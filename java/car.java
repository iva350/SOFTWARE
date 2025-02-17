public class Car {
    String license;
    Account driver;
    int passenger;

    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    public void printDataCar() {
        System.out.println("Number license: " + license + " Name driver: " + driver.name);
    }
}