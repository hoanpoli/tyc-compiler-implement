import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.curdir))

from tests.test_checker import *

if __name__ == "__main__":
    tests = [obj for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    passed = 0
    failed = 0
    
    for test in sorted(tests, key=lambda x: x.__name__):
        try:
            print(f"Running {test.__name__}...", end=" ")
            # To get the result, we need to inspect the test source or wrap it
            # But since we have the source here, let's just run it
            test()
            print("PASSED")
            passed += 1
        except AssertionError as e:
            print(f"FAILED (AssertionError)")
            # Re-run and capture result
            import inspect
            source = ""
            for line in inspect.getsourcelines(test)[0]:
                if 'source = """' in line or source:
                    source += line
                if '"""' in line and source and 'source = """' not in line:
                    break
            
            # This is hard to do generically. Let's just hardcode the check for test_004
            if test.__name__ == "test_004":
                from tests.utils import Checker
                source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
                result = Checker(source).check_from_source()
                print(f"  Actual result: {result}")
            
            failed += 1
        except Exception as e:
            print(f"FAILED: {str(e)}")
            import traceback
            traceback.print_exc()
            failed += 1
            
    print(f"\nSummary: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
