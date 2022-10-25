package ptvpso;

public class Particle {
    private double costValue;
    private Velocity velocity;
    private Position position;

    public Particle() {
            super();
    }

    public Particle(double costValue, Velocity velocity, Position location) {
            super();
            this.costValue = costValue;
            this.velocity = velocity;
            this.position = location;
    }

    public void setVelocity(Velocity velocity) {
            this.velocity = velocity;
    }

    public Velocity getVelocity() {
            return velocity;
    }

    public void setPosition(Position position) {
            this.position = position;
    }

    public Position getPosition() {
            return position;
    }

    public double getCostValue() {
            costValue = ProblemSet.evaluate(position);
            return costValue;
    }
}
