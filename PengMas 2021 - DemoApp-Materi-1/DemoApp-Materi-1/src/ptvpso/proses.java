/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
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
public class proses {
    /*
     * Proses PSO
     * Proses inisialisasi partikel
     * Proses menghitung fungsi obyektif PSO (cost)
     * Proses memperbarui kecepatan 
     * Proses memperbarui posisi partikel
     * Proses memperbarui pBest
     * Proses mencari gBest
     */
    
    private ArrayList<Particle> partikel = new ArrayList<>();
    private double[] pbest = new double[Parameter.getSWARM_SIZE()];
    private ArrayList<Position> pBestPos = new ArrayList<>();
    private double gbest;
    private Position gBestPos;
    private double[] cost = new double[Parameter.getSWARM_SIZE()];
    //public double N,P,K,p1,p2,p3,p4,p5;
    public ArrayList<HasilIterasi> hasilIterasi = new ArrayList<>();
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
              
                V0[j] = 0;
                Velocity velocity = new Velocity(V0);
                p.setVelocity(velocity);     
                
                partikel.add(i, p);   

                System.out.println(""+bulat(p.getPosition().getPos()[j])+ " ");
            }
          System.out.println("");
        }  
    }
    
    public void costValue(){
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            cost[i] = partikel.get(i).getCostValue();
        }
    }
    
    public void updatepbest(){
        for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
            if(cost[i] < pbest[i]){
                pbest[i] = cost[i];
                pBestPos.set(i, partikel.get(i).getPosition());
            }
        }
    }  
    
    public double MinCostPbest(){
        double min = cost[0];
        for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
            if(cost[i]<min){
                min = cost[i];
            }
        }
        return min;
    }
    
    public static int IndexMinPbest(double[] list) {
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
        int bestPartikelIndex = IndexMinPbest(pbest);
            if(pbest[bestPartikelIndex] < gbest) {
                gbest = pbest[bestPartikelIndex];
                gBestPos = partikel.get(bestPartikelIndex).getPosition();    
            }
            for (int i = 0; i < Parameter.getPROBLEM_DIMENSION(); i++) {
              gBestPos = partikel.get(bestPartikelIndex).getPosition(); 
              
               System.out.println(""+bulat(gBestPos.getPos()[i])+" ");
            }    
    }
  
    public double inersia (int t){   
        double w = ((Parameter.getW_MAX()-Parameter.getW_MIN())*((Parameter.getMAX_ITERATION()-(double)t)/Parameter.getMAX_ITERATION())+Parameter.getW_MIN());
        return w;
    }
    
    public double Vmax(int j){
        double[] Vmax = new double[Parameter.getPROBLEM_DIMENSION()];
        double Vm;
            Vmax[j] = Parameter.getK() * ((ProblemSet.max[j]-ProblemSet.min[j])/2); 
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
        System.out.println("-----Inisialisasi partikel-----");
        inisialisasi();

        System.out.println("-----Cost-----");
        costValue();
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            System.out.println (""+ bulat(cost[i]));
        }   
        
        System.out.println("-------pBest---------");
        for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
            for (int j=0; j<Parameter.getPROBLEM_DIMENSION(); j++) {
                //jika iterasi = 0, maka pBest = cost, posisi pBest = posisi partikel inisialisasi
                pbest[i] = cost[i]; 
                pBestPos.add(i,partikel.get(i).getPosition());
                System.out.print(""+ bulat(pBestPos.get(i).getPos()[j])+" ");
            }
            System.out.println("");
        }
  
        System.out.println("-------gBest---------");
        System.out.println("gBest : partikel ke-"+IndexMinPbest(pbest));
        System.out.println("fitness gBest: "+decimal(MinCostPbest()));
        System.out.println("posisi gBest: ");
        updategbest();
        
        //nilai r1 dan r2 dibangkitkan secara random
        double r1 = rand.nextDouble();
        double r2 = rand.nextDouble();
        System.out.println("r1 = "+bulat(r1));
        System.out.println("r2 = "+bulat(r2));
        
        //proses iterasi PSO
        int t = 1;
        while(t < Parameter.getMAX_ITERATION() +1) {
            HasilIterasi hasil = new HasilIterasi();         
            System.out.println("");
            System.out.println("ITERASI-"+t);
            
            //menghitung koefisien time-varying-inertia-weight (TVIW)
            double w = ((Parameter.getW_MAX()-Parameter.getW_MIN())*((Parameter.getMAX_ITERATION()-(double)t)/Parameter.getMAX_ITERATION())+Parameter.getW_MIN());
            System.out.println("inersia = "+bulat(w));
            
            //menghitung koefisien time-varying-acceleration (TVAC)
            double c1=(Parameter.getC1f()-Parameter.getC1i())*((double)t/Parameter.getMAX_ITERATION())+Parameter.getC1i();
            double c2=(Parameter.getC2f()-Parameter.getC2i())*((double)t/Parameter.getMAX_ITERATION())+Parameter.getC2i(); 
            System.out.println("c1 = "+bulat(c1));
            System.out.println("c2 = "+bulat(c2));
            
            for (int i = 0; i < Parameter.getSWARM_SIZE(); i++) {
                Particle p = partikel.get(i);
                //memperbarui kecepatan partikel
                double[] newVel = new double[Parameter.getPROBLEM_DIMENSION()];
                for (int j = 0; j < Parameter.getPROBLEM_DIMENSION(); j++) {
                    newVel[j] = (inersia(t) * p.getVelocity().getPos()[j]) + 
                                (r1 * c1) * (pBestPos.get(i).getPos()[j] - p.getPosition().getPos()[j]) +
                                (r2 * c2) * (gBestPos.getPos()[j] - p.getPosition().getPos()[j]);
                    //pembatasan kecepatan 
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
                
                //memperbarui posisi partikel
                double[] newPos = new double[Parameter.getPROBLEM_DIMENSION()];
                for(int j=0;j<Parameter.getPROBLEM_DIMENSION();j++){
                    newPos[j] = p.getPosition().getPos()[j] + newVel[j];
                    //pembatasan ruang pencarian atau dimensi partikel
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
            costValue();
            for(int i=0; i<Parameter.getSWARM_SIZE(); i++) {
                System.out.println (""+ bulat(cost[i]));
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
            System.out.println("GBest : partikel ke-"+IndexMinPbest(pbest));
            hasil.partikel = IndexMinPbest(pbest);
            System.out.println("Fitness gBest: "+bulat(MinCostPbest()));
            System.out.println("Posisi gBest: ");
            updategbest();
            
            //penyimpanan nilai gBest untuk ditampilkan dalam interface
            hasil.NPK = gBestPos.getPos()[0];
            hasil.urea_1 = gBestPos.getPos()[1];
            hasil.sp36_1 = gBestPos.getPos()[2];
            hasil.kcl_1 = gBestPos.getPos()[3];
            hasil.urea_2 = gBestPos.getPos()[4];
            hasil.urea_3 = gBestPos.getPos()[5];
            hasil.kcl_3 = gBestPos.getPos()[6];
            hasil.pest_1 = gBestPos.getPos()[7];
            hasil.pest_2 = gBestPos.getPos()[8];
            hasil.pest_3 = gBestPos.getPos()[9];
            hasil.pest_4 = gBestPos.getPos()[10];
            hasil.pest_5 = gBestPos.getPos()[11];
            hasil.cost = MinCostPbest();
            hasilIterasi.add(hasil);

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

class HasilIterasi{
    public int iterasi, partikel;
    public double NPK, urea_1, sp36_1, kcl_1, urea_2, urea_3, kcl_3, pest_1, pest_2, pest_3, pest_4, pest_5, cost;
}
