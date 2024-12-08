def main(test_mode=False, debug_level=0):
    """
    Demonstrate different behaviors based on build parameters
    
    :param test_mode: Boolean flag to enable test-specific behavior
    :param debug_level: Integer to control verbosity of output
    """
    # Condition 1: Based on test_mode parameter
    if test_mode:
        print("Running in TEST MODE")
        # Specific actions for test mode
        test_specific_action()
    else:
        print("Running in PRODUCTION MODE")
        production_specific_action()
    
    # Condition 2: Based on debug_level parameter
    if debug_level == 0:
        print("Debug: Mini logging")
    elif debug_level == 1:
        print("Debug: Stand logging")
        log_standard_info()
    elif debug_level >= 2:
        print("Debug: Verb logging")
        log_detailed_info()

def test_specific_action():
    """Perform actions specific to test mode"""
    print("  - Skipping heavy computations")
    print("  - Using mock data")

def production_specific_action():
    """Perform actions specific to production mode"""
    print("  - Running full computations")
    print("  - Using real data")

def log_standard_info():
    """Log standard level information"""
    print("  - Logging basic system metrics")
    print("  - Tracking key performance indicators")

def log_detailed_info():
    """Log detailed information for debugging"""
    print("  - Logging extensive system details")
    print("  - Capturing comprehensive performance metrics")
    print("  - Enabling advanced diagnostic tools")

if __name__ == "__main__":
    import sys
    
    # Default values
    test_mode = False
    debug_level = 0
    
    # Check for command-line arguments
    if len(sys.argv) > 1:
        # First argument can be test mode (true/false)
        test_mode = sys.argv[1].lower() == 'true'
    
    if len(sys.argv) > 2:
        # Second argument can be debug level
        try:
            debug_level = int(sys.argv[2])
        except ValueError:
            print("Invalid debug level. Using default (0)")
    
    # Call main function with parameters
    main(test_mode, debug_level)