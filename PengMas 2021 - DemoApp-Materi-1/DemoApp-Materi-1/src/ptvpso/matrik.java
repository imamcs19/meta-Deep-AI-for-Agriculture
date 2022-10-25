/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ptvpso;
import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Random;
import java.util.Vector;
/**
 *
 * @author Core_i5
 */
//public class matrik implements PSOParameter{
public class matrik {
    
    private Vector<Particle> partikel = new Vector<>();
    private double[] pbest = new double[Parameter.getSWARM_SIZE()];
    private ArrayList<Position> pBestPos = new ArrayList<>();
    private ArrayList<Position> sortingPos = new ArrayList<>();
    private double[] possort = new double[Parameter.getSWARM_SIZE()];
    private double gbest;
    private Position gBestPos, sortPos;
    private double[] fitness = new double[Parameter.getSWARM_SIZE()];
    public double N,P,K,p1,p2,p3,p4,p5;
    
    Random rand = new Random();
    
    public void inisialisasi() {
        Particle p; 
        
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            p = new Particle();
            double[] X = new double[Parameter.getPROBLEM_DIMENSION()];
            double[] V0 = new double[Parameter.getPROBLEM_DIMENSION()];

            for(int j=0; j<Parameter.getPROBLEM_DIMENSION(); j++){
                
                X[j] = ProblemSet.min[j] + rand.nextDouble() * (ProblemSet.max[j] - ProblemSet.min[j]);    
                Position location = new Position(X);
                p.setPosition(location);
              
                V0[j] = PSOParameter.V0;
                Velocity velocity = new Velocity(V0);
                p.setVelocity(velocity);     
                
                partikel.add(i, p);   
                
//                System.out.println(""+decimal(p.getPosition().getPos()[j])+ " ");
                System.out.print(""+bulat(p.getPosition().getPos()[j])+ " ");
            }
          System.out.println("");
        }  
    }
    
    public void fitnessvalue(){
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            fitness[i] = partikel.get(i).getCostValue();
        }
    }
    
    public void updatepbest(){
        for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
            if(fitness[i] < pbest[i]){
                pbest[i] = fitness[i];
                pBestPos.set(i, partikel.get(i).getPosition());
            }
        }
    }  
    
    public double minFpbest(){
        double min = fitness[0];
        for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
            if(fitness[i]<min){
                min = fitness[i];
            }
        }
        return min;
    }
    
    public static int getMinFitness(double[] list) {
        int pos = 0;
        double minValue = list[0];

        for(int i=0; i<list.length; i++) {
            if(list[i] < minValue) {
                pos = i;
                minValue = list[i];
            }
        }
        return pos;
    }
    
    public void updategbest(){
        int bestPartikelIndex = getMinFitness(pbest);
            if(pbest[bestPartikelIndex] < gbest) {
                gbest = pbest[bestPartikelIndex];
               // gBestPos = partikel.get(bestPartikelIndex).getPosition();    
            }
            for (int i = 0; i < Parameter.getPROBLEM_DIMENSION(); i++) {
              gBestPos = partikel.get(bestPartikelIndex).getPosition(); 
              System.out.println(""+ bulat(gBestPos.getPos()[i]));
        }    
    }
  
    public double inersia (int t){   
        double w = ((Parameter.getW_MAX()-Parameter.getW_MIN())*((Parameter.getMAX_ITERATION()-(double)t)/Parameter.getMAX_ITERATION())+Parameter.getW_MIN());
        return w;
    }
    
    public double Vmax(int j){
        double[] Vmax = new double[Parameter.getPROBLEM_DIMENSION()];
        double Vm;
            Vmax[j] = 0.6 * ((ProblemSet.max[j]-ProblemSet.min[j])/2); 
            Vm = Vmax[j];
        return Vm;
    }
    
    public double Vmin(int j){
        double[] Vmin = new double[Parameter.getPROBLEM_DIMENSION()];
        double Vm;
            Vmin[j] = -Vmax(j); 
            Vm = Vmin[j];
        return Vm;
    }
    
    
    
    public void execute() {
        
        System.out.println("-----Batas bawah-----");
        for(int j=0; j<Parameter.getPROBLEM_DIMENSION(); j++){
            System.out.print(""+ProblemSet.min[j]+" ");
        }
        System.out.println("");  
      
        System.out.println("-----Batas atas-----");
        for(int j=0; j<Parameter.getPROBLEM_DIMENSION(); j++){
            System.out.print(""+ProblemSet.max[j]+" ");
        }
        System.out.println("");
        
        System.out.println("-----Vmax-----");
        for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
            System.out.print(""+ bulat(Vmax(j))+ " ");
        }
        System.out.println("");
        
        System.out.println("-----Vmin-----");
        for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
            System.out.print(""+ bulat(Vmin(j))+ " ");
        }
        System.out.println("");
        
        System.out.println("-----PosAwal-----");
        inisialisasi();

        System.out.println("-----fitness-----");
        fitnessvalue();
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            System.out.println (""+ bulat(fitness[i]));
        }   
        
        System.out.println("-------pBest---------");
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            for (int j=0; j<Parameter.getPROBLEM_DIMENSION(); j++) {
                pbest[i] = fitness[i]; 
                pBestPos.add(i,partikel.get(i).getPosition());
                System.out.print(""+ bulat(pBestPos.get(i).getPos()[j])+" ");
            }
            System.out.println("");
        }
  
        System.out.println("-------gBest---------");
        System.out.println("gBest : partikel ke-"+getMinFitness(pbest));
        System.out.println("fitness gBest: "+decimal(minFpbest()));
        System.out.println("posisi gBest: ");
        updategbest();
        
        int t = 1;

        double r1 = rand.nextDouble();
        double r2 = rand.nextDouble();
        
        System.out.println("r1 = "+bulat(r1));
        System.out.println("r2 = "+bulat(r2));
        
        while(t < Parameter.getMAX_ITERATION() +1) {
            HasilIterasi hasil = new HasilIterasi();         
            System.out.println("");
            System.out.println("ITERASI-"+t);
            
            double c1=(Parameter.getC1f()-Parameter.getC1i())*((double)t/Parameter.getMAX_ITERATION())+Parameter.getC1i();
            double c2=(Parameter.getC2f()-Parameter.getC2i())*((double)t/Parameter.getMAX_ITERATION())+Parameter.getC2i(); 
            
            System.out.println("inersia = "+bulat(inersia(t)));
            System.out.println("c1 = "+bulat(c1));
            System.out.println("c2 = "+bulat(c2));

            for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
                Particle p = partikel.get(i);
                double[] newVel = new double[Parameter.getPROBLEM_DIMENSION()];
                for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
                    newVel[j] = (inersia(t) * p.getVelocity().getPos()[j]) + 
                                (r1 * c1) * (pBestPos.get(i).getPos()[j] - p.getPosition().getPos()[j]) +
                                (r2 * c2) * (gBestPos.getPos()[j] - p.getPosition().getPos()[j]);

                    if(newVel[j]>Vmax(j)){
                        newVel[j] = Vmax(j);
                    }else if(newVel[j]<Vmin(j)){
                        newVel[j] = Vmin(j);
                    }else{
                        newVel[j] = newVel[j];
                    }      
                }
                    Velocity vel = new Velocity(newVel);
                    p.setVelocity(vel);
                   
                    double[] newPos = new double[Parameter.getPROBLEM_DIMENSION()];
                    for(int j=0;j<Parameter.getPROBLEM_DIMENSION();j++){
                        newPos[j] = p.getPosition().getPos()[j] + newVel[j];

                        if(newPos[j]<ProblemSet.min[j]){
                            newPos[j] = ProblemSet.min[j];
                        }else if(newPos[j]>ProblemSet.max[j]){
                            newPos[j] = ProblemSet.max[j];
                        }else{
                            newPos[j] = newPos[j];
                        } 
                    }
                    Position loc = new Position(newPos);
                    p.setPosition(loc);
            }
            
            System.out.println("-------Vbaru---------");
            for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
                for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
                    System.out.print(""+bulat(partikel.get(i).getVelocity().getPos()[j])+" ");
                }
                System.out.println("");
            }
            
            System.out.println("-------Posbaru---------");
            for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
                for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
                    System.out.print(""+bulat(partikel.get(i).getPosition().getPos()[j])+" ");
                }
                System.out.println("");
            }
           
            System.out.println("-----Cost---------");
            fitnessvalue();
            for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
                System.out.println (""+ bulat(fitness[i]));
            }
            
            System.out.println("-----UpdatePbest---------");
            updatepbest();
            for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
                System.out.println(""+bulat(pbest[i]));
            }
            System.out.println("Posisi pBest: ");
            for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
                for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
                    System.out.print(""+bulat(pBestPos.get(i).getPos()[j])+" ");
                }
                System.out.println("");
            }
            
            System.out.println("-------UpdateGBest---------");
            System.out.println("GBest : partikel ke-"+getMinFitness(pbest));
            System.out.println("Fitness gBest: "+bulat(minFpbest()));
            System.out.println("Posisi gBest: ");
            updategbest();
            
            t++;
        } 
    }
    
    public static String decimal(double data){
        String hasil;
        DecimalFormat df = new DecimalFormat("#.###");
            hasil = df.format(data);
          
        return hasil;
    }
    
    public static double bulat(double r){  
        int decimalPlace = 3;  
        BigDecimal bd = new BigDecimal(r);  
        bd = bd.setScale(decimalPlace,BigDecimal.ROUND_UP);  
        r = bd.doubleValue(); 
        return r;
    }  
    



}