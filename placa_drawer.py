from PIL import Image, ImageFont, ImageDraw
import re


class Placa:
    def Desenhar(self, placa, tipo='carro', categoria='particular'):
        placa = self.Mercosul(placa)
        categoria = categoria.lower()
        if placa is None:
            return None
        if categoria == 'particular':
            cor_letra = (0, 0, 0, 255)
        elif categoria == 'oficial':
            cor_letra = (0, 51, 160, 255)
        elif categoria == 'especial':
            cor_letra = (0, 122, 83, 255)
        elif categoria == 'diplomatico':
            cor_letra = (242, 169, 0, 255)
        elif categoria == 'comercial':
            cor_letra = (200, 16, 46, 255)
        else:
            cor_letra = (129, 131, 135, 255)

        if tipo == 'carro':

            img = Image.open('./Placas/placa_carro_particular.png')
            placa_fonte = ImageFont.truetype('./Fonts/EuroPlate.ttf', 200)

            d = ImageDraw.Draw(img)

            d.text((70, 100), placa, font=placa_fonte, fill=cor_letra)

            return img
        else:

            img = Image.open('./Placas/placa_moto_particular.png')
            placa_fonte = ImageFont.truetype('./Fonts/EuroPlate.ttf', 100)
            placa_obj = placa.split(' ')

            d = ImageDraw.Draw(img)

            d.text((70, 50), placa_obj[0],
                   font=placa_fonte, fill=cor_letra)
            d.text((49, 140), placa_obj[1],
                   font=placa_fonte, fill=cor_letra)

            return img

    def Mercosul(self, placa):
        placa = placa.upper()

        if placa.find('-') != -1:
            placa = placa.replace('-', ' ')

        if len(placa) == 7:
            placa = placa[:3] + ' ' + placa[3:]

        placa_obj = re.match(
            r'([A-Z]{3}) [0-9]{1}([A-Z|0-9]{1})[0-9]{2}', placa)

        if placa_obj:
            try:
                numero = int(placa_obj.group(2))
                placa = placa[:5] + chr(ord('A') + numero) + placa[6:]
                return placa
            except:
                return placa
        else:
            return None
