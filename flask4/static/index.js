document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#form').onsubmit= ()=>{
        //Initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST','/convert');
        //callback function for when request complete
        request.onload = ()=>{
            //Extract JSON data from request 
            const data = JSON.parse(request.responseText);

            //update the result div
            if (data.success){
                const contents = '1 EUR is equal to ' + data.rate + ' ' + currency;
                document.querySelector('#result').innerHTML = contents;
            }
            else{
                document.querySelector('#result').innerHTML = "There was an error!";
            }
        };
        //add data to send with request 
        const data = new FormData();
        data.append('currency',currency);

        //send request
        request.send(data);
        return false;

    };
});