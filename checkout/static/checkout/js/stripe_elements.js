/* global Stripe */

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

  const card = elements.create('card');
  card.mount('#card-element');

  // Live validation errors
  card.addEventListener('change', (event) => {
    cardErrors.textContent = event.error ? event.error.message : '';
  });

  // Helper: toggle UI while processing
  function setLoading(isLoading) {
    if (submitButton) submitButton.disabled = isLoading;
    if (!loadingOverlay) return;

    if (isLoading) {
      loadingOverlay.classList.remove('d-none');
    } else {
      loadingOverlay.classList.add('d-none');
    }
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setLoading(true);
    cardErrors.textContent = '';

    // Grab billing details from your crispy fields (they usually use id_*)
    const fullName = document.getElementById('id_full_name');
    const email = document.getElementById('id_email');

    const result = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: fullName ? fullName.value.trim() : '',
          email: email ? email.value.trim() : '',
        },
      },
    });

    if (result.error) {
      cardErrors.textContent = result.error.message;
      setLoading(false);
      return;
    }

    // Success: submit form to Django (create Order, etc.)
    form.submit();
  });
})();
