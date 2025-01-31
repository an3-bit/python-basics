class CarDiagnosticSystem:
    def __init__(self, oil_level, coolant_level, air_filter_status, brake_pad_status, battery_status, tire_pressure,
                 spark_plug_status, transmission_status, fuel_filter_status, engine_warning):
        # Initialize sensor readings
        self.oil_level = oil_level
        self.coolant_level = coolant_level
        self.air_filter_status = air_filter_status
        self.brake_pad_status = brake_pad_status
        self.battery_status = battery_status
        self.tire_pressure = tire_pressure
        self.spark_plug_status = spark_plug_status
        self.transmission_status = transmission_status
        self.fuel_filter_status = fuel_filter_status
        self.engine_warning = engine_warning

    def check_oil(self):
        if self.oil_level < 30:
            return "Oil change required soon!"
        return "Oil level sufficient."

    def check_coolant(self):
        if self.coolant_level < 40:
            return "Coolant level low. Please add water/coolant."
        return "Coolant level is sufficient."

    def check_air_filter(self):
        if self.air_filter_status == "dirty":
            return "Air filter needs to be changed soon."
        return "Air filter is clean."

    def check_brakes(self):
        if self.brake_pad_status == "worn":
            return "Brake pads are worn. Service required soon."
        return "Brake pads are in good condition."

    def check_battery(self):
        if self.battery_status < 20:
            return "Battery health low. Please check or replace battery."
        return "Battery health is good."

    def check_tire_pressure(self):
        if any(pressure < 30 for pressure in self.tire_pressure):
            return "Tire pressure is low. Check all tires."
        return "Tire pressure is adequate."

    def check_spark_plugs(self):
        if self.spark_plug_status == "worn":
            return "Spark plugs are worn. Please replace soon."
        return "Spark plugs are in good condition."

    def check_transmission(self):
        if self.transmission_status == "faulty":
            return "Transmission issue detected. Visit the garage."
        return "Transmission is functioning properly."

    def check_fuel_filter(self):
        if self.fuel_filter_status == "dirty":
            return "Fuel filter needs to be replaced."
        return "Fuel filter is in good condition."

    def overall_check(self):
        checks = [
            self.check_oil(),
            self.check_coolant(),
            self.check_air_filter(),
            self.check_brakes(),
            self.check_battery(),
            self.check_tire_pressure(),
            self.check_spark_plugs(),
            self.check_transmission(),
            self.check_fuel_filter()
        ]

        # Determine if any major issues were found
        critical_issue = any("Service required" in check or "Visit the garage" in check for check in checks)
        print("\nMaintenance Updates:")
        for check in checks:
            print("- " + check)

        # Display warning if critical issues are found
        if critical_issue:
            print("\nWarning: Please visit the garage soon.")
        else:
            print("\nYour car is in good condition. You can drive now. Safe journey.")


def main():
    # Welcome message
    print("Hello Andrew, how are you today?")
    user_response = input("You: ").strip().lower()

    # Respond based on user's response
    if "not" in user_response or "bad" in user_response:
        print("Oh sorry to hear, but I believe you will be fine.")
    else:
        print("Great to hear!")

    # Ask if user wants to check the car's maintenance status
    print("Do you want to check the maintenance status of your car? (yes/no)")
    check_status = input("You: ").strip().lower()

    # Proceed with diagnostics if user says "yes"
    if check_status == "yes":
        # Simulated sensor data
        car = CarDiagnosticSystem(
            oil_level=25,  # Oil level in percentage
            coolant_level=35,  # Coolant level in percentage
            air_filter_status="dirty",  # Air filter condition
            brake_pad_status="good",  # Brake pad condition
            battery_status=15,  # Battery health percentage
            tire_pressure=[32, 31, 29, 30],  # Tire pressure for each tire in PSI
            spark_plug_status="good",  # Spark plug condition
            transmission_status="good",  # Transmission condition
            fuel_filter_status="dirty",  # Fuel filter condition (for diesel cars)
            engine_warning=False  # Engine warning light status
        )

        # Run the overall check
        car.overall_check()
    else:
        print("Okay, have a great day!")


# Run the main function to initiate the program
if __name__ == "__main__":
    main()
