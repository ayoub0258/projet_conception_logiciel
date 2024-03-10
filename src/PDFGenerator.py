from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import PageBreak
import qrcode
import tempfile

class PDFGenerator:
    @staticmethod
    def generate_pdf(tracks_info):
        print("Etape 8 : Generate one pdf containe trucks hitsters")
        doc = SimpleDocTemplate("info_chansons.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        style_title = styles["Title"]
        style_body = styles["BodyText"]
        content = []

        for track_info in tracks_info:
            title = Paragraph("Informations sur la chanson", style_title)
            content.append(title)
            content.append(Spacer(1, 12))

            content.append(Paragraph("<b>Titre:</b> {}".format(track_info['name']), style_body))
            content.append(Paragraph("<b>Artiste:</b> {}".format(track_info['artist_name']), style_body))
            content.append(Paragraph("<b>Année de sortie:</b> {}".format(track_info['release_date']), style_body))
            content.append(Paragraph("<b>URL Spotify:</b> {}".format(track_info['spotify_url']), style_body))

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(track_info['spotify_url'])
            qr.make(fit=True)

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                qr_img = qr.make_image(fill_color="black", back_color="white")
                qr_img.save(temp_file.name)
                content.append(Spacer(1, 12))
                content.append(Paragraph("<b>QR Code de l'URL Spotify</b>", style_body))
                content.append(Image(temp_file.name, width=200, height=200))

            content.append(Spacer(1, 24))
            content.append(PageBreak())

        doc.build(content)
