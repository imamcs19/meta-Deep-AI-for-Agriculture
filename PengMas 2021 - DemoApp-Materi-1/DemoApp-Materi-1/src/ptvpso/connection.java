/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package ptvpso;

/**
 *
 * @author Core_i5
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.*;

public class connection {
    private Connection koneksi;
    
    public Connection connect(){
       //untuk koneksi ke driver
       try{
           Class.forName("com.mysql.jdbc.Driver");
           System.out.println("berhasil load driver");
       }catch(ClassNotFoundException cnfe){
           System.out.println("Tidak ada Driver "+cnfe);
       }
       //untuk koneksi ke database
       try{
           String url="jdbc:mysql://localhost:3306/ptvpso";
           koneksi=DriverManager.getConnection(url,"root","");
           System.out.println("Berhasil koneksi");
       }catch(SQLException se){
           System.out.println("Gagal koneksi "+se);
           //JOptionPane.showMessageDialog(null,"Gagal koneksi...MySQL server belum aktif");
       }
       return koneksi;
    }
}