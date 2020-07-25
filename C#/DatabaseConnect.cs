using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using MySql.Data.MySqlClient;

namespace DatabaseApp
{
    class Program
    {

        static void Main(string[] args)
        {
           Console.WriteLine("Podaj system kt�ry wybieraasz: 1.MsSQL 2.MySQL ");
            string numerek;
            numerek = Console.ReadLine();

            string ConnectionString = "xxx";


            if (numerek == "1")
            {
                ConnectionString = "SERVER = mssql-2016.labs.wmi.amu.edu.pl; DATABASE = dbad_s434788; USER ID = xxx; PASSWORD = xxx ";
                SqlConnection sqlconn = new SqlConnection(ConnectionString);

                using (sqlconn)
                {
                    string x;
                    Console.WriteLine("Podaj nazw� tabelki do odczytania: ");
                    x = Console.ReadLine();



                    sqlconn.Open();
                    SqlCommand cmd = new SqlCommand("SELECT * FROM " + x, sqlconn);


                    using (SqlDataReader reader = cmd.ExecuteReader())
                    {
                        var columns = new List<string>();

                        for (int i = 0; i < reader.FieldCount; i++)
                        {
                            columns.Add(reader.GetName(i));
                        }

                        columns.ForEach(i => Console.Write("{0}\t", i));
                        Console.WriteLine("\n");
                        while (reader.Read())
                        {
                            for (int i = 0; i < reader.FieldCount; i++)
                            {
                                Console.Write(String.Format("{0} |", reader[i]));

                            }
                            Console.WriteLine("");
                        }

                        reader.Close();
                        sqlconn.Close();
                    }
                    Console.WriteLine("Oto twoja tabelka. naci�nij enter aby wyj��.");
                    Console.ReadLine();

                }
            }
            else
            {
                ConnectionString = "SERVER= mysql.wmi.amu.edu.pl; DATABASE= s434788_BazaDanych; UID= xxx; PASSWORD= xxx; SslMode=none ";
                MySqlConnection sqlconn1 = new MySqlConnection(ConnectionString);

                using (sqlconn1)
                {
                    string x;
                    Console.WriteLine("Podaj nazw� tabelki do odczytania: ");
                    x = Console.ReadLine();



                    sqlconn1.Open();
                    MySqlCommand cmd = new MySqlCommand("SELECT * FROM " + x, sqlconn1);
                    

                    using (MySqlDataReader dataReader = cmd.ExecuteReader())
                    {
                        var columns = new List<string>();

                        for (int i = 0; i < dataReader.FieldCount; i++)
                        {
                            columns.Add(dataReader.GetName(i));
                        }

                        columns.ForEach(i => Console.Write("{0}\t", i));
                        Console.WriteLine("\n");
                        while (dataReader.Read())
                        {
                            for (int i = 0; i < dataReader.FieldCount; i++)
                            {
                                Console.Write(String.Format("{0} |", dataReader[i]));

                            }
                            Console.WriteLine("");
                        }

                        dataReader.Close();
                        sqlconn1.Close();
                    }
                    Console.WriteLine("Oto twoja tabelka. naci�nij enter aby wyj��.");
                    Console.ReadLine();

                }
            }         
            
        }
    }
}