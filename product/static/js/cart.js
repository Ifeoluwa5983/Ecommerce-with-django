const cart_btn = document.getElementsByClassName('update-cart');

for (let i = 0; i < cart_btn.length; i++){
    cart_btn[1].addEventListener('click', function (){
        const productId = this.dataset.product;
        const action = this.dataset.action;
        console.log('productId:', productId, 'action:', action)

    console.log('user:', user)
    if (user === 'AnonymousUser'){
        console.log("You are not logged in")
    }else{
        updateUserOrder(productId, action)
    }
})
}

function updateUserOrder(productId, action) {
    console.log("You are logged in, sending data...")

    var url = '/update-item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },body:JSON.stringify({'productId': productId, 'action': action})
    })

        .then((response) =>{
        return response.json()
    })

     .then((data) =>{
        console.log('data:', data)
    })
}