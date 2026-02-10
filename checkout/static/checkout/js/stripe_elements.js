/* global Stripe */

/*
  Core logic/payment flow inspired by:
  https://stripe.com/docs/payments/accept-a-payment
*/

(function () {
  const form = document.getElementById('payment-form');
  if (!form) return;

  const submitButton = document.getElementById('submit-button');
  const cardErrors = document.getElementById('card-errors');
  const loadingOverlay = document.getElementById('loading-overlay');

  // Prefer json_script values (safer), fallback to dataset
  const publicKeyEl = document.getElementById('id_stripe_public_key');
  const clientSecretEl = document.getElementById('id_client_secret');

  const stripePublicKey = publicKeyEl
    ? JSON.parse(publicKeyEl.textContent)
    : form.dataset.publicKey;

  const clientSecret = clientSecretEl
    ? JSON.parse(clientSecretEl.textContent)
    : form.dataset.clientSecret;

  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();

  // Optional: style (matches course-ish look)
  const style = {
    base: {
      color: '#000',
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': { color: '#aab7c4' },
    },
    invalid: {
      color: '#dc3545',
      iconColor: '#dc3545',
    },
  };

  const card = elements.create('card', { style });
  card.mount('#card-element');

  // Realtime validation errors
  card.addEventListener('change', (event) => {
    if (event.error) {
      cardErrors.textContent = event.error.message;
    } else {
      cardErrors.textContent = '';
    }
  });

  // "Fade toggle" without jQuery (simple + reliable)
  function setProcessing(isProcessing) {
    // Disable only Stripe + submit (do NOT disable CSRF or hidden inputs)
    card.update({ disabled: isProcessing });
    if (submitButton) submitButton.disabled = isProcessing;

    // Visually hide/disable the form UI (but keep inputs enabled so CSRF submits)
    form.style.opacity = isProcessing ? '0.5' : '1';
    form.style.pointerEvents = isProcessing ? 'none' : 'auto';

    // Show/hide overlay
    if (loadingOverlay) {
      loadingOverlay.classList.toggle('d-none', !isProcessing);
    }
  }

  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    setProcessing(true);

    const fullName = document.getElementById('id_full_name');
    const email = document.getElementById('id_email');

    const result = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card,
        billing_details: {
          name: fullName ? fullName.value.trim() : '',
          email: email ? email.value.trim() : '',
        },
      },
    });

    if (result.error) {
      cardErrors.textContent = result.error.message;
      setProcessing(false);
      return;
    }

    if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
      form.submit();
      return;
    }

    // Fallback
    setProcessing(false);
  });
})();
