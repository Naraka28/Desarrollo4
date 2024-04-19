/*
* To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author dii
 */
class Menu {
    int level;
    String type;
    String menu;
    String menu_text;
    ArrayList<Menu> submenu;

    public Menu(int level, String type, String menu, String menu_text) {
        this.level = level;
        this.type = type; //USER or ADMIN
        this.menu = menu;
        this.menu_text = menu_text; //Display text
        this.submenu = null;
    }
    public void addSubMenu(Menu parent,Menu child) {
        if (parent!=null) {
            if (parent.submenu!=null) {
                parent.submenu.add(child);
            }else{
                parent.submenu = new ArrayList<Menu>();
                parent.submenu.add(child);
            }
        }
}
}

public class LoginMysql {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws NoSuchAlgorithmException {
        // TODO code application logic here
        String prg_user = "daniel@gmail.com";
        String prg_pwd  = "jicama";
        byte[] hashed = getSHA(prg_pwd);
        String hashed64 = hexString(hashed);
        System.out.println("Hashed:"+hashed);
        System.out.println("Hashed64:"+hashed64);
        String URL = "jdbc:mysql://148.225.60.126/disneyplus?useSSL=false&useTimezone=true&serverTimezone=UTC&allowPublicKeyRetrieval=true";
        String db_user = "disney";
        String db_password = "Ma58toAa!YLtT9S9";
        Connection conexion = getConnectionMySQL(URL, db_user, db_password, prg_user,prg_pwd);
        if (conexion!=null){
            System.out.println("Bienvenido! "+prg_user);
            mainCycle(conexion,prg_user);
        } else {
            System.out.println("Acceso denegado a :"+prg_user);
        }
        try {
           conexion.close();
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
    public static void mainCycle(Connection cnx, String user){
        ArrayList<Menu> menu_list = getOptionMenu(cnx, user);
        Menu parent=menu_list.get(0);
        for (Menu menu: menu_list){
            if(menu.level%10==0){
                parent=menu;
            }else{
                parent.addSubMenu(parent, menu);
            }
        }
        String option = "0";
        do{
            showMenu(menu_list);
            option=getMenu(menu_list);
            System.out.println(option);
            executeMenuOption(cnx, option,user);
        }while(!option.equals("0"));
    }
    public static void executeMenuOption(Connection cnx, String option,String user){
        String SQL="";
        switch (option) {
            case "LIST_USERS":
                SQL="SELECT username,email,role FROM user_dan";
                listRecords(SQL,cnx);
                break;
            case "LIST_SHOWS":
                SQL="SELECT * FROM shows LIMIT 0,40";
                listRecords(SQL,cnx);
                break;
            case "TOP_RATINGS":
                SQL="SELECT * FROM vista_ratings_todos LIMIT 10";
                listRecords(SQL,cnx);
                break;
            case "TOPTEN_RATING":
                SQL="SELECT * FROM `vies_estrada_ratings` LIMIT 0,10";
                listRecords(SQL,cnx);
                break;
            case "ADD_RATING":
                addRating(cnx,user);
                break;
            case "MOD_RATING":
                modRating(cnx,user);
                break;
            case "DEL_RATING":
                delRating(cnx,user);
                break;

            case "UPDATE_USER":
                break;

            default:
                break;
        }
    }
    public static void modRating(Connection cnx, String user){
        String SQL="SELECT ratings_DIEN.id, ratings_DIEN.id_show, shows.title,ratings_DIEN.rating, ratings_DIEN.timestamp FROM ratings_DIEN,shows,users WHERE users.email=? AND users.id=ratings_DIEN.id_user AND ratings_DIEN.id_show=shows.show_id ORDER BY timestamp DESC";
        try {
            PreparedStatement ps=cnx.prepareStatement(SQL);
            ps.setString(1, user);
            SQL=ps.toString();
            SQL=SQL.substring(SQL.indexOf(":")+1);
            System.out.println("SQL:"+SQL);
            System.out.println();
            listRecords(SQL, cnx);
    }catch(Exception e){
        e.printStackTrace();
    }
}
    public static void delRating(Connection cnx, String user){
        String SQL="SELECT ratings_DIEN.id, ratings_DIEN.id_show, shows.title,ratings_DIEN.rating, ratings_DIEN.timestamp FROM ratings_DIEN,shows,users WHERE users.email=? AND users.id=ratings_DIEN.id_user AND ratings_DIEN.id_show=shows.show_id ORDER BY timestamp DESC";
        try {
            PreparedStatement ps=cnx.prepareStatement(SQL);
            ps.setString(1, user);
            SQL=ps.toString();
            SQL=SQL.substring(SQL.indexOf(":")+1);
            System.out.println("SQL:"+SQL);
            System.out.println();
            listRecords(SQL, cnx);
            System.out.println("¿Qué registro deseas borra?:>");
            Scanner scan = new Scanner(System.in);
            int registro = scan.nextInt();
            System.out.println("A borrar registro: "+registro);
            //Autocommit lo hacemos falso
            cnx.setAutoCommit(false);
            SQL = "DELETE FROM ratings_DIEN WHERE id = ?";
            ps = cnx.prepareStatement(SQL);
            ps.setInt(1, registro);;
            int r = ps.executeUpdate();
            //Obtenemos name
            System.out.println("User:"+user);
            SQL = "SELECT id,name FROM `users` WHERE email = ?";
            ps = cnx.prepareStatement(SQL);
            ps.setString(1, user);
            ResultSet rs = ps.executeQuery();
            int id=0;
            String name="";
            while (rs.next()) {
                id = rs.getInt(1);
                name =rs.getString(2);
            }
            //Actualizamos ratings para user
            SQL = "UPDATE users a INNER JOIN (SELECT COUNT(*) AS num_reviews FROM vista_ratings_DIEN WHERE name=? GROUP BY name) b SET a.reviews = b.num_reviews WHERE a.name = ?";
            ps = cnx.prepareStatement(SQL);
            ps.setString(1, name);
            ps.setString(2, name);
            System.out.println(ps.toString());
            int ru = ps.executeUpdate();
            //Final
            cnx.commit();
            System.out.println("Se borraron "+r+" registros en ratings");
            System.out.println("Se actualizaron "+ru+" registros en users");
    }catch(Exception e){
        e.printStackTrace();
    }
}
    public static void addRating(Connection cnx, String user) {
        Scanner scan = new Scanner(System.in); 
        System.out.print("Busca show o película:");
        String show = scan.nextLine();
        show = "%"+show+"%";
        String SQL = "SELECT show_id, title FROM shows WHERE title LIKE ? ORDER BY title";
        try {
            //autocommit lo hacemos FALSO
            cnx.setAutoCommit(false);
            PreparedStatement ps = cnx.prepareStatement(SQL);
            ps.setString(1, show);
            SQL = ps.toString();
            SQL = SQL.substring(SQL.indexOf(":")+1); // hack
            System.out.println("SQL:"+SQL);
            listRecords(SQL,cnx);
            // GET USER ID
            System.out.println("User:"+user);
            SQL = "SELECT id,name FROM `users` WHERE email = ?";
            ps = cnx.prepareStatement(SQL);
            ps.setString(1, user);
            ResultSet rs = ps.executeQuery();
            int id=0;
            String name="";
            while (rs.next()) {
                id = rs.getInt(1);
                name =rs.getString(2);
            }
            System.out.println("id:"+id);
            System.out.print("Show a calificar:");
            show = scan.nextLine();
            System.out.print("Comentario:");
            String comentario = scan.nextLine();
            System.out.print("Calificación [0 a 5]:");
            int rating = scan.nextInt();
            SQL = "INSERT INTO ratings_bob (id_user,id_show,rating,comments) VALUES (?,?,?,?)";
            ps = cnx.prepareStatement(SQL);
            ps.setInt(1, id);
            ps.setString(2,show);
            ps.setInt(3,rating);
            ps.setString(4, comentario);
            System.out.println(ps.toString());
            int r = ps.executeUpdate();
            System.out.println("Inserted records:"+r);
            SQL = "UPDATE users a INNER JOIN (SELECT COUNT(*) AS num_reviews FROM vista_ratings WHERE name=? GROUP BY name) b SET a.reviews = b.num_reviews WHERE a.name = ?";
            ps = cnx.prepareStatement(SQL);
            ps.setString(1, name);
            ps.setString(2, name);
            System.out.println(ps.toString());
            r = ps.executeUpdate();
            System.out.println("Updated "+r+" records...");
            cnx.commit();
        } catch (Exception ex) {
            System.out.println("addRating:"+ex.getMessage());
        }
    }

    public static void displayRecords(ResultSet rs){
        try{
            ResultSetMetaData rsmd = rs.getMetaData();
            int columnsNumber = rsmd.getColumnCount();
            for (int i = 1; i <= columnsNumber; i++) {
                System.out.printf("%29s ",rsmd.getColumnName(i));
            }
            while (rs.next()) {
                System.out.println();
                for (int i = 1; i <= columnsNumber; i++) {
                    System.out.printf("%29s ",rs.getString(i));
                }
            }System.out.println("\n");
        }catch(Exception ex){
            System.out.println("displayRecords():"+ex.getMessage());
        }
    }

    private static void listRecords(String SQL, Connection cnx) {
        try{
            PreparedStatement ps= cnx.prepareStatement(SQL);
            ResultSet rs= ps.executeQuery();
            displayRecords(rs);
        }catch(Exception ex){
            System.out.println("listUsers():"+ex.getMessage());
        }
    }



    public static String getMenu(ArrayList <Menu> menuList){
        Scanner scan = new Scanner(System.in);
        System.out.println(" 0: Salir");
        System.out.println("Seleccione una opción: ");
        String option=scan.nextLine();
        if (!option.equals("0")){
            int idx=Integer.parseInt(option);
            option=menuList.get(idx).menu;
        }
        return option;
    }

    public static void showMenu(ArrayList<Menu> menu_list){
        int i =0;
        for (Menu menu : menu_list) {
            if(menu.level%10==0){
                System.out.println("** "+menu.menu_text+" **");
            } else {
                System.out.println(" "+i+":"+menu.menu_text);
            }
            i++;

        }
    }

    public static ArrayList<Menu> getOptionMenu(Connection cnx, String user) {
        ArrayList<Menu> menu_list = new ArrayList<Menu>();
        String query_user = "SELECT * FROM menu_dan,user_dan WHERE  user_dan.email = ? AND menu_dan.user_role = user_dan.role ORDER BY level" ;
        String query_admin= "SELECT * FROM menu_dan,user_bob WHERE  user_dan.email = ? AND menu_dan.user_role = user_dan.role ORDER BY level";
        String query ="";
        query = query_user;
        try {
            PreparedStatement ps = cnx.prepareStatement(query);
            ps.setString(1,user);
            ResultSet rs = ps.executeQuery();
            while (rs.next()== true) {
                String type = rs.getString(1);
                String menu = rs.getString(2);
                int level =   rs.getInt(3);
                String menu_text = rs.getString(4);
                Menu menu_row = new Menu(level,type,menu,menu_text);
                menu_list.add(menu_row);
            }

        } catch (Exception ex) {
            System.out.println("getOptionMenu:"+ex.getMessage());
        }
        return menu_list;
    }

    public static Connection getConnectionMySQL(String URL, String db_user,String db_password, String prg_user, String prg_password){
        Connection cnx = null;
        try {
            cnx = DriverManager.getConnection(URL, db_user, db_password);
            System.out.println("Succesful connection to DB");
            String SQL = "SELECT username FROM user_dan WHERE email=? AND password=SHA2(?,256)";
            PreparedStatement psu =cnx.prepareStatement(SQL);
            psu.setString(1, prg_user);
            psu.setString(2, prg_password);
            ResultSet rsu = psu.executeQuery();
            if (!rsu.next()) {
                cnx.close();
                cnx = null;
            }
        } catch (Exception ex) {
            System.out.println("getConnection():"+ex.getMessage());
        }
        return cnx;
    }
    public static byte[] getSHA(String input) throws NoSuchAlgorithmException {
    byte[] hash = null;
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            hash = md.digest(input.getBytes(StandardCharsets.UTF_8));
        } catch (Exception ex) {
            System.out.println("getSHA: "+ex.getMessage());
        }
        return hash;
    }
    public static String hexString(byte[] hash) {
        BigInteger number = new BigInteger(1, hash);
        StringBuilder hexString = new StringBuilder(number.toString(16));
        while (hexString.length()< 32){
            hexString.insert(0,'0');
        }
        return hexString.toString();
    }
}

