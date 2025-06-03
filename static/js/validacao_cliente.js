document.addEventListener('DOMContentLoaded', function () {
  // Seleciona todos os formulários que devem usar essa validação
  const forms = document.querySelectorAll('.formPessoa');

  forms.forEach(form => {

    function mostrarErro(campoId, mensagem) {
      const input = form.querySelector(`#${campoId}`);
      input.classList.add('is-invalid');

      let feedback = input.nextElementSibling;
      if (!feedback || !feedback.classList.contains('invalid-feedback')) {
        feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        input.parentNode.insertBefore(feedback, input.nextSibling);
      }
      feedback.textContent = mensagem;
    }

    function limparErros() {
      ['id_nome', 'id_fone', 'id_email'].forEach(id => {
        const input = form.querySelector(`#${id}`);
        if (!input) return;
        input.classList.remove('is-invalid');
        const feedback = input.nextElementSibling;
        if (feedback && feedback.classList.contains('invalid-feedback')) {
          feedback.remove();
        }
      });
    }

    form.addEventListener('submit', async function (event) {
      event.preventDefault();
      limparErros();

      const nomeInput = form.querySelector('#id_nome');
      const foneInput = form.querySelector('#id_fone');
      const emailInput = form.querySelector('#id_email');

      if (!nomeInput || !foneInput || !emailInput) {
        console.error('Campos do formulário não encontrados.');
        return;
      }

      const nome = nomeInput.value.trim();
      const fone = foneInput.value.trim();
      const email = emailInput.value.trim();

      const verificacaoUrl = form.getAttribute('data-verificacao-url');
      const csrfToken = form.getAttribute('data-csrf');

      let erro = false;

      if (nome.length === 0 || nome.length > 50) {
        mostrarErro('id_nome', 'Nome é obrigatório e deve ter até 50 caracteres.');
        erro = true;
      }

      const telefoneRegex = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/;
      if (!telefoneRegex.test(fone)) {
        mostrarErro('id_fone', 'Telefone inválido.');
        erro = true;
      }

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        mostrarErro('id_email', 'E-mail inválido.');
        erro = true;
      }

      if (erro) return;

      // Verificação AJAX
      try {
        const response = await fetch(verificacaoUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
          },
          body: JSON.stringify({ fone, email })
        });

        const data = await response.json();
        if (data.fone_existe) {
          mostrarErro('id_fone', 'Telefone já cadastrado.');
          return;
        }
        if (data.email_existe) {
          mostrarErro('id_email', 'E-mail já cadastrado.');
          return;
        }

        // Tudo certo, envia o formulário
        form.submit();

      } catch (err) {
        console.error(err);
        alert('Erro ao verificar duplicidade. Tente novamente.');
      }
    });
  });
});
