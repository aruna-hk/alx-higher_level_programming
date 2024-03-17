#!/usr/bin/python3

""" create database script using Mysql database connector """

import MySQLdb
import sys

userinfo = {"user":sys.argv[1], "password":sys.argv[2], "db":sys.argv[3], "port":3306}
query = "CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa"
query2 = """ use hbtn_0e_0_usa; CREATE TABLE IF NOT EXISTS states 
            (id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(256) NOT NULL,PRIMARY KEY (id);
            INSERT INTO states (name) VALUES \"California\"),
            (\"Arizona\"), (\"Texas\"), (\"New York\"),\(\"Nevada\");
)"""
connection = MySQLdb.connect(**userinfo)
connection.query(query)
connection.query(query2)
