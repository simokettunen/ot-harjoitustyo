import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')
        
    def test_rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.6')
        
    def test_saldo_vahenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(6)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.04')
        
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')
        
    def test_ota_rahaa_palauttaa_true_jos_rahat_riittavat(self):
        value = self.maksukortti.ota_rahaa(6)
        self.assertTrue(value)
        
    def test_ota_rahaa_palauttaa_false_jos_rahat_eivat_riita(self):
        value = self.maksukortti.ota_rahaa(11)
        self.assertFalse(value)
        