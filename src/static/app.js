const enlaceNosotros=document.getElementById("enlace-nosotros")
const infoNosotos=document.getElementById("info-nosotros")
const infoContacto=document.getElementById("info-contacto")
const enlaces=document.querySelectorAll("#enlaces a")
let opa=document.getElementById("opacity")
const cerrarNosotros=document.getElementById("cerrar-nosotros")
const cerrarContacto=document.getElementById("cerrar-contacto")

const msj=document.getElementById("msj")




enlaces.forEach(enlace => {
    enlace.addEventListener("click",(e)=>{
        e.preventDefault();
        valor=enlace.textContent
        
        if (valor === "Nosotros"){
            infoNosotos.classList.toggle("show")
            infoContacto.classList.remove("show")

            cerrarNosotros.addEventListener("click",()=>{
                infoNosotos.classList.remove("show")
                opa.classList.remove("show-opacity")
                    })
            if(infoNosotos.classList.contains("show")){
                 opa.classList.add("show-opacity")
            }else if(!infoNosotos.classList.contains("show")){
                opa.classList.remove("show-opacity")        
            }               
        }else if(valor==="Contacto"){
            infoContacto.classList.toggle("show")
            infoNosotos.classList.remove("show")

            cerrarContacto.addEventListener("click",()=>{
            infoContacto.classList.remove("show")
            opa.classList.remove("show-opacity")
                })

            if(infoContacto.classList.contains("show")){
                opa.classList.add("show-opacity")
           }else if(!infoContacto.classList.contains("show")){
               opa.classList.remove("show-opacity")        
           }
        
        }else{
            console.log("ubicacioon")
        }
        
    })
    
});


