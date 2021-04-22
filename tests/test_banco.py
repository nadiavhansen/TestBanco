from unittest import TestCase, mock
from funcoes.banco import *
from datetime import date


class TestBanco(TestCase):

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="0;0;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_validar_dados_do_cartao_is_working(self, mock_datetime):
        mock_datetime.today.return_value = date(2021, 4, 1)
        mock_datetime.strptime.return_value = date(2024, 10, 1)
        resultado = Banco().validar_dados_do_cartao("0", {"numero": "0",
                                                          "senha": "0",
                                                          "valor_compra": 80.0})
        resultado_falso = Banco().validar_dados_do_cartao("0", {"numero": "10",
                                                          "senha": "10",
                                                          "valor_compra": 80000.0})
        self.assertTrue(resultado)
        self.assertFalse(resultado_falso)

        mock_datetime.today.assert_called_once()

    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_credito")
    @mock.patch("funcoes.banco.Banco.efetuar_pagamento_com_cartao_debito")
    def test_efetuar_pagamento_is_working(self, mock_credito, mock_debito):
        mock_credito.return_value = True
        mock_debito.return_value = True

        Banco().efetuar_pagamento("0", {})
        Banco().efetuar_pagamento("1", {})


    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="0;0;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.Banco.validar_dados_do_cartao")
    def test_efetuar_pagamento_com_cartao_credito_is_working(self, mock_validar):
        mock_validar.side_effect = [True, False]

        dados = dict(numero="0", valor_compra=500)
        resultado = Banco().efetuar_pagamento_com_cartao_credito(dados)
        resultado_falso = Banco().efetuar_pagamento_com_cartao_credito(dados)

        self.assertTrue(resultado)
        self.assertFalse(resultado_falso)


    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="0;0;10/24;165;500;799.0"))
    @mock.patch("funcoes.banco.Banco.validar_dados_do_cartao")
    def test_efetuar_pagamento_com_cartao_debito_is_working(self, mock_validar):
        mock_validar.side_effect = [True, False]
        dados = dict(numero="0", valor_compra=300)
        resultado = Banco().efetuar_pagamento_com_cartao_debito(dados)
        resultado_falso = Banco().efetuar_pagamento_com_cartao_debito(dados)


        self.assertTrue(resultado)
        self.assertFalse(resultado_falso)


    # def test_gerar_boleto_is_working(self):
    #     dados = dict(valor=0.0, data=0000, codigo="123", conta_loja="000124578")
    #     dados_esperados = {"valor": 0.0,"data_validade": 0000,"código": "123", "conta_loja": "000124578"}
    #     resultado = Banco().gerar_boleto(dados)
    #     self.assertDictEqual(resultado, dados_esperados)


    @mock.patch("funcoes.banco.Banco")
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_gerar_codigo_boleto_is_working(self, mock_datetime, mock_banco):
        mock_datetime.now.return_value = "0000-00-00 00:00:00.000000"
        mock_banco.codigo_banco.return_value = "180"

        dados = dict(valor=10.56)
        resultado = Banco().gerar_codigo_boleto(dados)
        self.assertEqual(resultado, "180000000000000000000001056")

        mock_datetime.now.assert_called_once()
