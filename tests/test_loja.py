# from unittest import TestCase, mock
# from funcoes.loja import *
#
#
# class TestLoja(TestCase):
#
#     # @mock.patch("funcoes.banco.Banco.efetuar_pagamento")
#     # def test_solicitar_pagamento_com_cartao_is_working(self, mock_pagamento):
#     #     mock_pagamento.side_effect = [True, False]
#     #     dados = dict(numero="0", senha="0", valor_compra=10)
#     #     self.assertTrue(dados)
#     #     self.assertFalse(dados)
#
#
#
#     def test_solicitar_boleto(self):
#
#         pass
#     #
#     # def test_efetuar_pagamento_com_dinheiro_is_working(self):
#     #     pass
#     #
#     #
#     #
#     #
#     #
#     @mock.patch("funcoes.banco.Banco.efetuar_pagamento")
#     def test_solicitar_pagamento_com_cartao_is_working(self, mock_pagamento):
#         dados = dict(numero=1234, senha=3322)
#
#         mock_pagamento.return_value = True
#         result = Loja().solicitar_pagamento_com_cartao(dados, 10, "0")
#         self.assertEqual(result, "Compra efetuada com sucesso!")
#
#         mock_pagamento.return_value = False
#         result = Loja().solicitar_pagamento_com_cartao(dados, 10, "1")
#         self.assertEqual(result, "Compra efetuada com fracasso!")
