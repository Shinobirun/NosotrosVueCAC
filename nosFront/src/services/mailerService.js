const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'nosotrosMunTurismo@gmail.com',
    pass: 'N0s0tr0s2023'
  }
});

const enviarCorreo = (consulta) => {
  const mailOptions = {
    from: 'nosotrosMunTurismo@gmail.com',
    to: 'nosotrosMunTurismo@gmail.com',
    subject: 'Nueva consulta',
    text: `Nombre: ${consulta.nombre}\nEmail: ${consulta.email}\nMensaje: ${consulta.mensaje}`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.log('Error al enviar el correo:', error);
    } else {
      console.log('Correo enviado:', info.response);
    }
  });
};

module.exports = {
  enviarCorreo,
};
