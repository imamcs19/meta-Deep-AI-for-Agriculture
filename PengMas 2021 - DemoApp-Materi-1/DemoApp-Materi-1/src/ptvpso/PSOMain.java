
package ptvpso;

import java.util.Scanner;
import javax.swing.Box;
import javax.swing.JFrame;

public class PSOMain {
    public static String N,P,K,P1,P2,P3,P4,P5;
    public static int ppk;
    public static double n,p,k,p1,p2,p3,p4,p5;
    public static String opt1,opt2,opt3,opt4,opt5;
    public static String pes1,pes2,pes3,pes4,pes5;
    public static void main(String args[]) {
        
        Scanner input = new Scanner(System.in);
        
//        System.out.println("Pilih jenis lahan");
//        System.out.println("1. Ladang/Lahan kering (Padi Gogo)");
//        System.out.println("2. Lahan Sawah (Padi Sawah)");
//        System.out.println("Pilih lahan(1/2):");
//        lhn = input.nextInt();
//        System.out.println("");
//        switch(lhn){
//            case 1:
//            case 2:
//            
//        }
        
//        System.out.println("Pilihan jenis pupuk");
//        System.out.println("1. Tunggal");
//        System.out.println("2. Tunggal + jerami");
//        System.out.println("3. Tunggal + pupuk kandang");
//        System.out.println("4. Tunggal + majemuk phonska 15:15:15");
//        System.out.println("5. Tunggal + majemuk phonska 10:10:10");
//        System.out.println("6. Tunggal + majemuk phonska 30:6:8");
//        System.out.print("Pilih pupuk(1/2/3/4/5/6):");
//        ppk = input.nextInt();
//        System.out.println("");
//        
//        System.out.println("Status N");
//        System.out.println("1. Rendah");
//        System.out.println("2. Sedang");
//        System.out.println("3. Tinggi");
//        System.out.print("Pilih tanah(1/2/3):");
//        N = input.next();
//        System.out.println("");
//        
//        System.out.println("Status P");
//        System.out.println("1. Rendah");
//        System.out.println("2. Sedang");
//        System.out.println("3. Tinggi");
//        System.out.print("Pilih tanah(1/2/3):");
//        P = input.next();
//        System.out.println("");
//        
//        System.out.println("Status K");
//        System.out.println("1. Rendah");
//        System.out.println("2. Sedang");
//        System.out.println("3. Tinggi");
//        System.out.print("Pilih tanah(1/2/3):");
//        K = input.next();
//        System.out.println("");       
//        
//        switch(N){
//            case "1":
//                n=135;
//                break;
//            case "2":
//                n=112.5;
//                break;
//            case "3":
//                n=109;
//                break;
//        }     
//        switch(P){
//            case "1":
//                p=45;
//                break;
//            case "2":
//                p=27;
//                break;
//            case "3":
//                p=18; 
//                break;
//        } 
//        switch(K){
//            case "1":
//                k=60;
//                break;
//            case "2":
//                k=45;
//                break;
//            case "3":
//                k=30;
//                break;
//        }
//        
//        System.out.println("Pilihan OPT");
//        System.out.print("1. Wereng coklat Y/T : ");
//        opt1 = input.next();
//        System.out.print("2. Penggerek batang Y/T :");
//        opt2 = input.next();
//        System.out.print("3. Walang sangit Y/T :");
//        opt3 = input.next();
//        System.out.print("4. Hawar Y/T :");
//        opt4 = input.next();
//        System.out.print("5. Bercak daun Y/T :");
//        opt5 = input.next();
//        System.out.println("");
//        
//        switch(opt1){
//            case "y":
//                pes1 = "y";
//                System.out.println("Status AE OPT1");
//                System.out.println("1. <AE");
//                System.out.println("2. >AE");
//                System.out.println("3. =AE");
//                System.out.print("Pilih tanah(1/2/3):");
//                P1 = input.next();
//                System.out.println("");
//                
//                switch(P1){
//                    case "1":
//                        p1=0.5;
//                        break;
//                    case "2":
//                        p1=1;
//                        break;
//                    case "3":
//                        p1=1;
//                        break;
//                }
//                
//            case "t": 
//                break;
//        }
//        
//        switch(opt2){
//            case "y":
//                pes2 = "y";
//                System.out.println("Status AE OPT2");
//                System.out.println("1. <AE");
//                System.out.println("2. >AE");
//                System.out.println("3. =AE");
//                System.out.print("Pilih tanah(1/2/3):");
//                P2 = input.next();
//                System.out.println("");
//                
//                switch(P2){
//                    case "1":
//                        p2=0.75;
//                        break;
//                    case "2":
//                        p2=1;
//                        break;
//                    case "3":
//                        p2=1;
//                        break;
//                }
//                
//            case "t": 
//                break;
//        }
//        
//        switch(opt3){
//            case "y":
//                pes3 = "y";
//                System.out.println("Status AE OPT3");
//                System.out.println("1. <AE");
//                System.out.println("2. >AE");
//                System.out.println("3. =AE");
//                System.out.print("Pilih tanah(1/2/3):");
//                P3 = input.next();
//                System.out.println("");
//                
//                switch(P3){
//                    case "1":
//                        p3=0.2;
//                        break;
//                    case "2":
//                        p3=0.4;
//                        break;
//                    case "3":
//                        p3=0.4;
//                        break;
//                }
//                
//            case "t": 
//                break;
//        }
//        
//        switch(opt4){
//            case "y":
//                pes4 = "y";
//                System.out.println("Status AE OPT4");
//                System.out.println("1. <AE");
//                System.out.println("2. >AE");
//                System.out.println("3. =AE");
//                System.out.print("Pilih tanah(1/2/3):");
//                P4 = input.next();
//                System.out.println("");
//                
//                switch(P4){
//                    case "1":
//                        p4=0.25;
//                        break;
//                    case "2":
//                        p4=0.5;
//                        break;
//                    case "3":
//                        p4=0.5;
//                        break; 
//                }
//                
//            case "t": 
//                break;
//        }
//        
//        switch(opt5){
//            case "y":
//                pes5 = "y";
//                System.out.println("Status AE OPT5");
//                System.out.println("1. <AE");
//                System.out.println("2. >AE");
//                System.out.println("3. =AE");
//                System.out.print("Pilih tanah(1/2/3):");
//                P5 = input.next();
//                System.out.println("");
//                
//                switch(P5){
//                    case "1":
//                        p5=0.5;
//                        break;
//                    case "2":
//                        p5=1;
//                        break;
//                    case "3":
//                        p5=1;
//                        break;
//                }
//                
//            case "t": 
//                break;
//        }
////        System.out.println("p1= "+p1+" ,p2= "+p2+" ,p3= "+p3+" ,p4= "+p4+" ,p5= "+p5);
//
//        new ProblemSet().cekGen(ppk);
//        new ProblemSet().cekPest(pes1,pes2,pes3,pes4,pes5);
//        new ProblemSet().set(ppk,n, p, k, p1, p2, p3, p4, p5);
//        new matrik().execute();
        
        Interface frame = new Interface();
        frame.setLocationRelativeTo(null);
        //        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
//        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);
        
    }
}
