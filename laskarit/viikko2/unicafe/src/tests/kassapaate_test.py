import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    def test_kassapaate_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kateisosto_toimii_rahaa_tarpeeksi_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 60)
        
    def test_kateisosto_toimii_rahaa_ei_tarpeeksi_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 200)
        
    def test_kateisosto_toimii_rahaa_tarpeeksi_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 50)
        
    def test_kateisosto_toimii_rahaa_ei_tarpeeksi_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 300)
        
    def test_korttiosto_toimii_rahaa_tarpeeksi_edullinen(self):
        maksukortti = Maksukortti(1000)
        value = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(maksukortti), 'saldo: 7.6')
        self.assertTrue(value)
        
    def test_korttiosto_toimii_rahaa_ei_tarpeeksi_edullinen(self):
        maksukortti = Maksukortti(100)
        value = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(maksukortti), 'saldo: 1.0')
        self.assertFalse(value)
        
    def test_korttiosto_toimii_rahaa_tarpeeksi_maukas(self):
        maksukortti = Maksukortti(1000)
        value = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(maksukortti), 'saldo: 6.0')
        self.assertTrue(value)
        
    def test_korttiosto_toimii_rahaa_ei_tarpeeksi_maukas(self):
        maksukortti = Maksukortti(100)
        value = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(maksukortti), 'saldo: 1.0')
        self.assertFalse(value)
        
    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        self.assertEqual(str(maksukortti), 'saldo: 15.0')
        
    def test_lataa_rahaa_ei_lataa_negatiivista_rahamaaraa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(maksukortti), 'saldo: 10.0')