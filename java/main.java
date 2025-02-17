public class Main {
    public static void main(String[] args) {
        System.out.println("Initializing...");
        System.out.println("Car...");
        Car car = new Car("AMR23", new Account("Adrian Newey", "AWJ1235", "newey@amr.com", "12365"));
        car.passenger = 4;
        car.printDataCar();

        System.out.println("Uberx...");
        UberX uberx = new UberX("FA14MR", new Account("Fernando Alonso", "JKL12365", "fernando@amr.com", "125478"), "Aston Martin", "AMR23");
        uberx.printDataCar();

        System.out.println("User...");
        User user = new User("Maria Del Prado", "SDG560859", "mariaoli@hotmail.com", "42921805");
        user.printDataUser();
    }