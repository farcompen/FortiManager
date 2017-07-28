#! /usr/bin  python
# -*- coding: utf-8 -*-

import sys

hosgeldin = """
                  ******************************************
                    FortiManager Uygulamasına Hoşgeldiniz
                       Çankırı KHB Bilgi Sistemleri
                                2017
                  ******************************************
"""
print(hosgeldin)
from pexpect import pxssh
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
try:
    session = pxssh.pxssh()
    session.force_password = True
    ip_Adres = raw_input("Firewall ip adresi :")
    fortiuser = raw_input("Kullanıcı:")
    fortipass = getpass.getpass("parola:")

    session.login(ip_Adres, fortiuser, fortipass, auto_prompt_reset=False)
    print("Bilgiler yükleniyor..Bu işlem 10 saniye sürebilir")
    session.sendline("get system performance status  ")

    session.prompt()
    dosya = open("session_before.txt", "w")
    dosya.write(session.before)
    dosya.flush()
    dosya.close()
    session.logout()
    session.close()

except pxssh.ExceptionPexpect as e:
    print(e)
    sys.exit()


def oku(parametre):
    dosya = open("session_before.txt", "r")
    if parametre == 1:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("Average network"):
                print(okunan)
                a = 1
    if parametre == 2:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("Memory"):
                print(okunan)
                a = 1
    if parametre == 3:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("CPU"):
                print(okunan)
                a = 1
    if parametre == 4:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("Average sessions"):
                print(okunan)
                a = 1
    if parametre == 5:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("IPS"):
                print(okunan)
                ips=okunan.strip()
                print(ips)
                a = 1
    if parametre == 6:
        a = 0
        while a == 0:
            okunan = dosya.readline()
            if okunan.startswith("Virus"):
                print(okunan)
                a = 1


islem = """

   ******************************************************
          1- Network Kullanım Durumu
          2- Ram Kullanımı
          3- CPU Kullanımı
          4- Session  Sayısı
          5- Saldırı log bilgisi
          6- Antivirüs log bilgisi
          { Çıkış için Sıfır'a basın }
   ******************************************************


"""
try:
    print(islem)

    deger = input("lütfen işlem numarası giriniz:")
    while deger != 0:
        oku(int(deger))
        deger = input("lütfen işlem numarası giriniz:")
        if deger == 0:
            print("çıkış yapıldı")
            sys.exit()
except ValueError as e:
    print(e)


