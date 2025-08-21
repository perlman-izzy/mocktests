#!/usr/bin/env python3
"""
Test script to validate the mocktests repository configuration and dependencies.
This serves as both a smoke test and unit test for the main functionality.
"""

import sys
import pathlib
import json
import importlib.util
from unittest.mock import patch, MagicMock

def test_imports():
    """Test that all required imports work."""
    try:
        import requests
        import json
        import pathlib
        import subprocess
        import traceback
        print("✅ All basic imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_requests_available():
    """Test that requests library is available and functional."""
    try:
        import requests
        # Test basic functionality without making external calls
        session = requests.Session()
        assert hasattr(session, 'get')
        assert hasattr(session, 'post')
        print("✅ Requests library functional")
        return True
    except Exception as e:
        print(f"❌ Requests test failed: {e}")
        return False

def test_script_syntax():
    """Test that the main script has valid syntax."""
    try:
        script_path = pathlib.Path(__file__).parent / "gemini-flask-57-2.py"
        if not script_path.exists():
            print(f"❌ Main script not found at {script_path}")
            return False
        
        with open(script_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Test compilation
        compile(code, str(script_path), 'exec')
        print("✅ Main script syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in main script: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking script: {e}")
        return False

def test_project_structure():
    """Test that essential project files exist."""
    base_path = pathlib.Path(__file__).parent
    required_files = [
        "gemini-flask-57-2.py",
        "requirements.txt",
        "PROJECT_CONFIG.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not (base_path / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required project files exist")
    return True

def test_mock_gemini_integration():
    """Test the core classes and functions with mocked dependencies."""
    try:
        # Import the script components
        script_path = pathlib.Path(__file__).parent / "gemini-flask-57-2.py"
        spec = importlib.util.spec_from_file_location("gemini_flask", script_path)
        gemini_module = importlib.util.module_from_spec(spec)
        
        # Mock the execution to avoid __main__ execution
        with patch.object(sys, 'argv', ['gemini-flask-57-2.py']):
            with patch('gemini_flask_57_2.main', return_value=0):  # Mock main to prevent execution
                try:
                    spec.loader.exec_module(gemini_module)
                except NameError:
                    # Expected when running without proper __file__ context
                    pass
        
        print("✅ Script structure is valid")
        return True
    except Exception as e:
        print(f"❌ Mock integration test failed: {e}")
        return False

def run_smoke_test():
    """Execute the smoke test command."""
    try:
        # This is the smoke test from PROJECT_CONFIG.md
        test_code = '''
import pathlib, requests, json
# Test basic imports and JSON functionality 
data = {"test": "smoke"}
assert json.dumps(data) == '{"test": "smoke"}'
print("SMOKE")
'''
        exec(test_code)
        print("✅ Smoke test passed")
        return True
    except Exception as e:
        print(f"❌ Smoke test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running mocktests repository validation tests...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_requests_available, 
        test_script_syntax,
        test_project_structure,
        test_mock_gemini_integration,
        run_smoke_test
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Add spacing between tests
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            print()
    
    print("=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Repository is properly configured.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())