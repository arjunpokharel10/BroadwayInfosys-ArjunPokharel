class Robot {
    String name;
    String color;
    int wright;
    

Robot(String n, String c, int w) {
    this.name = n;
    this.color = c;
    this.weight = w;
}

void introducceSelf() {
    System.out.println(
        "My name is " + this.name);
}
}

Robot r1 = 
    new Robot("Tom", "red", 30);

Robot r2 = 
    new Robot("Jerry", "blue", 40)

r1.introducceSelf();
r2.introducceSelf();


// Robot r1 = new Robot();
// r1.name = "Tom";
// r1.color = "red";
// r1.weight = 30;

// Robot r2 = new Robot();
// r2.name = "Jerry";
// r2.color = "blue";
// r2.weight = 40;
