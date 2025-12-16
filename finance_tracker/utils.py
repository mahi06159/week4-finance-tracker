def get_float_input(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please enter a valid number.")
