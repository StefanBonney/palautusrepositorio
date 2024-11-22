import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            return {1: 10, 2: 10}.get(tuote_id, 0)
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            return {
                1: Tuote(1, "maito", 5),
                2: Tuote(2, "leipä", 3)
            }.get(tuote_id, None)
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        """
        Aloitetaan asiointi, koriin lisätään tuote, jota varastossa on ja suoritetaan ostos, eli kutsutaan metodia kaupan tilimaksu, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumeroilla ja summalla
        Tämä siis on muuten copypaste esimerkistä, mutta assert_called_with-metodia käytettävä, jotta voidaan tarkastaa, että parametreilla on oikeat arvo
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_kaksi_eri_tuotetta(self):
        """
        Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta, joita varastossa on ja suoritetaan ostos, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 8)

    def test_kaksi_samaa_tuotetta(self):
        """
        Aloitetaan asiointi, koriin lisätään kaksi samaa tuotetta, jota on varastossa tarpeeksi ja suoritetaan ostos, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 10)

    def test_tuote_varastossa_ja_tuote_loppu(self):
        """
        Aloitetaan asiointi, koriin lisätään tuote, jota on varastossa tarpeeksi ja tuote joka on loppu ja suoritetaan ostos, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla
        """
        # override varasto_mock 
        def varasto_saldo(tuote_id):
            return {1: 10, 2: 0}.get(tuote_id, 0)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        """
        Varmista, että metodin aloita_asiointi kutsuminen nollaa edellisen ostoksen tiedot (eli edellisen ostoksen hinta ei näy uuden ostoksen hinnassa)
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "67890")
        self.pankki_mock.tilisiirto.assert_called_with("matti", 42, "67890", ANY, 3)

    def test_viitenumero_on_uusi_jokaiselle_maksutapahtumalle(self):
        """
        Varmista, että kauppa pyytää uuden viitenumeron jokaiselle maksutapahtumalle
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "67890")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        """
        Tarkasta viikoilla 1 ja 2 käytetyn coveragen avulla mikä on luokan Kauppa testauskattavuus.
        Jotain taitaa puuttua. Lisää testi
        """
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.varasto_mock.palauta_varastoon.assert_called_once_with(self.varasto_mock.hae_tuote(1))
