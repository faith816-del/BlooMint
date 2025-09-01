// Future JS will go here 🚀

// Flip card mobile + keyboard support
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card').forEach(card => {
    // click/tap toggles
    card.addEventListener('click', (e) => {
      card.classList.toggle('is-flipped');
      const pressed = card.classList.contains('is-flipped');
      card.setAttribute('aria-pressed', pressed);
    });

    // keyboard: Enter or Space toggles
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        card.classList.toggle('is-flipped');
        const pressed = card.classList.contains('is-flipped');
        card.setAttribute('aria-pressed', pressed);
      }
      if (e.key === 'Escape') {
        card.classList.remove('is-flipped');
        card.setAttribute('aria-pressed', false);
      }
    });
  });
});

// Simple slideshow for Custom Period Pack
let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.getElementsByClassName("slide");
  if (!slides || slides.length === 0) return;
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1; }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 3000);
}

// ------------------------
// Shop Cart Logic
// ------------------------
const shopCartDisplay = document.getElementById('shop-cart-display');

function displayShopCart() {
  const shopCart = JSON.parse(localStorage.getItem('shopCart')) || [];
  if (shopCart.length > 0) {
    shopCartDisplay.innerHTML = `<p>Shop Cart: ${shopCart.map(item => item.name).join(', ')}</p>`;
  } else {
    shopCartDisplay.innerHTML = `<p>Shop Cart is empty.</p>`;
  }
}

displayShopCart();


const addToCartBtns = document.querySelectorAll('.add-to-cart');

addToCartBtns.forEach(btn => {
  btn.addEventListener('click', (event) => {
    event.preventDefault();

    
    const productName = btn.getAttribute('data-name');
    const productPrice = btn.getAttribute('data-price');

    let shopCart = JSON.parse(localStorage.getItem('shopCart')) || [];
    shopCart.push({ name: productName, price: productPrice });
    localStorage.setItem('shopCart', JSON.stringify(shopCart));

    displayShopCart();

    alert('${productName} added to cart!');
    console.log('Current cart:', shopCart);
  });
});
