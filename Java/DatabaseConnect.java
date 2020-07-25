package database;

import java.sql.*;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner reader = new Scanner(System.in); // Reading from System.in

		System.out.println("Wybierz system bazodanowy: 1.MsSQL 2.MySQL : ");
		int numerek = reader.nextInt();

		if (numerek == 1) {
			try {

				Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver").newInstance();
				String url = "jdbc:sqlserver://mssql-2016.labs.wmi.amu.edu.pl ;databaseName=dbad_s434788";
				
				System.out.println("Connecting database...");
				Connection conn = DriverManager.getConnection(url, "s434788", "O3i23n17gU");
				System.out.println("Database connected!");
				
				System.out.println("Podaj Nazwê tabelki do sprawdzenia: ");
				String tabelka = reader.next();

				Statement stmt = conn.createStatement();
				ResultSet rs;

				rs = stmt.executeQuery("select * from " + tabelka);
				ResultSetMetaData rsmd = rs.getMetaData();

				String Nazwy = "";

				for (int j = 1; j <= rsmd.getColumnCount(); j++) {
					Nazwy += rsmd.getColumnName(j) + ", ";
				}

				System.out.println(Nazwy);

				System.out.println();

				while (rs.next()) {
					String row = "";
					for (int j = 1; j <= rsmd.getColumnCount(); j++) {
						row += rs.getString(j) + ", ";
					}
					System.out.println(row);
				}

				conn.close();
				reader.close();

				System.out.println("Oto twoja tabelka!");
				
			} catch (Exception e) {
				System.err.println("Got an exception! ");
				System.err.println(e.getMessage());
			}
		}
		else {
			try {	
			String url = "jdbc:mysql://mysql.wmi.amu.edu.pl:3306/s434788_BazaDanych?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
			String username = "s434788";
			String password = "Kanapka789";

			System.out.println("Connecting database...");
			Connection conn = DriverManager.getConnection(url, username, password );
			System.out.println("Database connected!");
			
			
			System.out.println("Podaj Nazwê tabelki do sprawdzenia: ");
			String tabelka = reader.next();

			Statement stmt = conn.createStatement();
			ResultSet rs;

			rs = stmt.executeQuery("select * from " + tabelka);
			ResultSetMetaData rsmd = rs.getMetaData();

			String Nazwy = "";

			for (int j = 1; j <= rsmd.getColumnCount(); j++) {
				Nazwy += rsmd.getColumnName(j) + ", ";
			}

			System.out.println(Nazwy);

			System.out.println();

			while (rs.next()) {
				String row = "";
				for (int j = 1; j <= rsmd.getColumnCount(); j++) {
					row += rs.getString(j) + ", ";
				}
				System.out.println(row);
			}

			System.out.println("Oto twoja tabelka!");
			
			conn.close();
			reader.close();
			
		} catch (Exception e) {
			System.err.println("Got an exception! ");
			System.err.println(e.getMessage());
		}
	}
}
}