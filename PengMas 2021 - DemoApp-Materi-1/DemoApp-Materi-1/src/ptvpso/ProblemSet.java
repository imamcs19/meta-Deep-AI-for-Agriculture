package ptvpso;
import ptvpso.connection;
import java.sql.SQLException;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

//public class ProblemSet implements PSOParameter{
public class ProblemSet {
    

    static java.sql.Connection conn = new connection().connect();

    public static double[] min = new double [Parameter.getPROBLEM_DIMENSION()];
    public static double[] max = new double [Parameter.getPROBLEM_DIMENSION()];

    public static void cekGen(int pil){
        if(pil == 1){
            try {
                String sql1 = "Select * from batasminpupuk where id='1'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='1'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 2){
            try {
                String sql1 = "Select * from batasminpupuk where id='2'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='2'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 3){
            try {
                String sql1 = "Select * from batasminpupuk where id='3'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='3'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 4){ //npk 15:15:15
            try {
                String sql1 = "Select * from batasminpupuk where id='4'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='4'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 5){ //npk 10:10:10
            try {
                String sql1 = "Select * from batasminpupuk where id='5'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='5'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 6){
            try {
                String sql1 = "Select * from batasminpupuk where id='6'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='6'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
        
        if(pil == 7){
            try {
                String sql1 = "Select * from batasminpupuk where id='7'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl1 = stm.executeQuery(sql1);
                while (rsl1.next()) {
                    min[0] = rsl1.getDouble("NPK");
                    min[1] = rsl1.getDouble("urea-1");
                    min[2] = rsl1.getDouble("sp36-1");
                    min[3] = rsl1.getDouble("kcl-1");
                    min[4] = rsl1.getDouble("urea-2");
                    min[5] = rsl1.getDouble("urea-3");
                    min[6] = rsl1.getDouble("kcl-3");
                }
            }catch(Exception e) {}
            try {
                String sql2 = "Select * from batasmaxpupuk where id='7'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl2 = stm.executeQuery(sql2);
                while (rsl2.next()) {
                    max[0] = rsl2.getDouble("NPK");
                    max[1] = rsl2.getDouble("urea-1");
                    max[2] = rsl2.getDouble("sp36-1");
                    max[3] = rsl2.getDouble("kcl-1");
                    max[4] = rsl2.getDouble("urea-2");
                    max[5] = rsl2.getDouble("urea-3");
                    max[6] = rsl2.getDouble("kcl-3");
                }
            }catch(Exception e) {}
        }
    }

    
    public static void cekPest(String opt1,String opt2,String opt3,String opt4,String opt5){
        if(opt1 == "y"){
            try {
                String sql = "Select * from pilihanpest where id='1'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl = stm.executeQuery(sql);
                while (rsl.next()) {
                    min[7] = rsl.getDouble("minKonsentrasi");
                    max[7] = rsl.getDouble("maxKonsentrasi");  
                }
            } catch (Exception e) {}
        }else{
            min[7] = max[7] = 0;
        }
        
        if(opt2 == "y"){
            try {
                String sql = "Select * from pilihanpest where id='2'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl = stm.executeQuery(sql);
                while (rsl.next()) {
                    min[8] = rsl.getDouble("minKonsentrasi");
                    max[8] = rsl.getDouble("maxKonsentrasi");  
                }
            } catch (Exception e) {}
        }else{
            min[8] = max[8] = 0;
        }
        
        if(opt3 == "y"){
            try {
                String sql = "Select * from pilihanpest where id='3'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl = stm.executeQuery(sql);
                while (rsl.next()) {
                    min[9] = rsl.getDouble("minKonsentrasi");
                    max[9] = rsl.getDouble("maxKonsentrasi");  
                }
            } catch (Exception e) {}
        }else{
            min[9] = max[9] = 0;
        }
        
        if(opt4 == "y"){
            try {
                String sql = "Select * from pilihanpest where id='4'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl = stm.executeQuery(sql);
                while (rsl.next()) {
                    min[10] = rsl.getDouble("minKonsentrasi");
                    max[10] = rsl.getDouble("maxKonsentrasi");  
                }
            } catch (Exception e) {}
        }else{
            min[10] = max[10] = 0;
        }
        
        if(opt5 == "y"){
            try {
                String sql = "Select * from pilihanpest where id='5'";
                java.sql.Statement stm = conn.createStatement();
                java.sql.ResultSet rsl = stm.executeQuery(sql);
                while (rsl.next()) {
                    min[11] = rsl.getDouble("minKonsentrasi");
                    max[11] = rsl.getDouble("maxKonsentrasi");  
                }
            } catch (Exception e) {}
        }else{
            min[11] = max[11] = 0;
        }
    }
    
    
    public static double n,p,k,ps1,ps2,ps3,ps4,ps5;
    public static int pil;
    public void set(int pilih,double N,double P,double K,double p1,double p2,double p3,double p4,double p5){
        pil = pilih;
        n = N;
        p = P;
        k = K;
        ps1=p1;
        ps2=p2;
        ps3=p3;
        ps4=p4;
        ps5=p5;
    }
    public static double getpil(){
        return pil;
    }
    public static double getN(){
        return n;
    }
    public static double getP(){
        return p;
    }
    public static double getK(){
        return k;
    }
    public static double getP1(){
        return ps1;
    }
    public static double getP2(){
        return ps2;
    }
    public static double getP3(){
        return ps3;
    }
    public static double getP4(){
        return ps4;
    }
    public static double getP5(){
        return ps5;
    }



    public static double evaluate(Position pos) {
        double result = 0;
        double ureaNPK,sp36NPK,kclNPK;
        //mengambil nilai posisi partikel setiap dimensi
        double npk1 = pos.getPos()[0]; 
        double urea1 = pos.getPos()[1]; 
        double sp36 = pos.getPos()[2];
        double kcl1 = pos.getPos()[3];
        double urea2 = pos.getPos()[4];
        double urea3 = pos.getPos()[5];
        double kcl2 = pos.getPos()[6];
        double pes1 = pos.getPos()[7]; 
        double pes2 = pos.getPos()[8]; 
        double pes3 = pos.getPos()[9];
        double pes4 = pos.getPos()[10];
        double pes5 = pos.getPos()[11];
        /*
         * menghitung kandungan N, P dan K dalam pupuk majemuk NPK phonska
         * Untuk membuat Pupuk yang setara dengan 50 Kg NPK Ponska (15 : 15 : 15) maka kita butuh :
         * Urea : ((15 : 100) X 50 Kg) X (100 : 46) = 13,8 Kg Urea
         * SP36 : ((15 : 100) X 50 Kg) X (100 : 36) = 20,8 Kg SP36
         * KCl : ((15 : 100) X 50 Kg) X (100 : 60) = 16,66 Kg KCl
         */
        if(getpil() == 4){ //NPK 15:15:15
             ureaNPK = ((0.15*npk1)*(100/46)); 
             sp36NPK = ((0.15*npk1)*(100/36));
             kclNPK  = ((0.15*npk1)*(100/60));
        }else if(getpil() == 5){ //NPK 10:10:10
             ureaNPK = ((0.10*npk1)*(100/46)); 
             sp36NPK = ((0.10*npk1)*(100/36));
             kclNPK  = ((0.10*npk1)*(100/60));
         }else if(getpil() == 6){ //NPK 30:6:8
             ureaNPK = ((0.30*npk1)*(100/46)); 
             sp36NPK = ((0.06*npk1)*(100/36));
             kclNPK  = ((0.08*npk1)*(100/60));
         }else{
             ureaNPK = 0; 
             sp36NPK = 0;
             kclNPK  = 0;
         }
        //menghitung kandungan N total, P total dan K total 
        double ntot = proses.bulat(0.46*(ureaNPK+urea1+urea2+urea3));
        double ptot = proses.bulat(0.36*(sp36NPK+sp36));
        double ktot = proses.bulat(0.6*(kclNPK+kcl1+kcl2));
        double hrgurea = 0;
        double hrgsp36 = 0;
        double hrgkcl = 0;
        double hrgnpk = 0;
        double hrgpest1 = 0;
        double hrgpest2 = 0;
        double hrgpest3 = 0;
        double hrgpest4 = 0;
        double hrgpest5 = 0;

        try {
            String sql = "Select * from hargapupuk where id='1'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgurea = rsl.getDouble("harga"); 
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from hargapupuk where id='2'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgsp36 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from hargapupuk where id='3'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgkcl = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from hargapupuk where id='4'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgnpk = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from pilihanpest where id='1'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgpest1 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from pilihanpest where id='2'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgpest2 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from pilihanpest where id='3'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgpest3 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from pilihanpest where id='4'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgpest4 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        try {
            String sql = "Select * from pilihanpest where id='5'";
            java.sql.Statement stm = conn.createStatement();
            java.sql.ResultSet rsl = stm.executeQuery(sql);
            while (rsl.next()) {
                hrgpest5 = rsl.getDouble("harga");
            }
        } catch (Exception e) {}
        
        //menghitung cost pupuk
        
        
        double resultppk = (((npk1*hrgnpk)+(urea1*hrgurea)+(sp36*hrgsp36)+(kcl1*hrgkcl)+(urea2*hrgurea)+(urea3*hrgurea)+(kcl2*hrgkcl))+
                       ((Math.abs(getN()-ntot)+Math.abs(getP()-ptot)+Math.abs(getK()-ktot))*10000));
        //menghitung cost pestisida
        double resultpest = (((pes1*hrgpest1)+((Math.abs(getP1()-pes1))*10000))+((pes2*hrgpest2)+((Math.abs(getP2()-pes2))*10000))+((pes3*hrgpest3)+((Math.abs(getP3()-pes3))*10000))+
            ((pes4*hrgpest4)+((Math.abs(getP4()-pes4))*10000))+((pes5*hrgpest5)+((Math.abs(getP5()-pes5))*10000)));
        //menghitung cost total
        result = resultppk+resultpest;
        
        
        System.out.println("N "+getN()+" ,P "+getP()+" ,K "+getK());
        System.out.println("p1 "+getP1()+" ,p3 "+getP3()+" ,p5 "+getP5());
        System.out.println("harga npk= "+hrgnpk+" urea= "+hrgurea+" sp36= "+hrgsp36+" kcl= "+hrgkcl);
        System.out.println("harga pes1= "+hrgpest1+" pes2= "+hrgpest2+" pes3= "+hrgpest3+" pes4= "+hrgpest4+" pes5= "+hrgpest5);
        System.out.println("ntot= "+ntot+" ,ptot= "+ptot+" ,ktot= "+ktot);
        System.out.println("selisihN= "+Math.abs(getN()-ntot)+" ,selisihP= "+Math.abs(getP()-ptot)+" ,selisihK= "+Math.abs(getK()-ktot));
        System.out.println("selisihP1= "+Math.abs(getP1()-pes1)+" ,selisihP2= "+Math.abs(getP2()-pes2)+" ,selisihP3= "+Math.abs(getP3()-pes3)+" ,selisihP4= "+Math.abs(getP4()-pes4)+" ,selisihP5= "+Math.abs(getP5()-pes5));
        System.out.println("fppk= "+resultppk+" ,fpest= "+resultpest);
        System.out.println("");

        return result;
    }
        

}
