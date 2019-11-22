function confirmarEliminar(id){
    Swal.fire({
        title: 'Seguro que quieres eliminar?',
        text: "no podrás devolverlo",
        icon: 'Cuidado',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!',
        cancelButtonText:'Cancelar'
      }).then((result) => {
        if (result.value) {
          window.location.href = "/eliminar-cena/"+id+"/";
          
        }
      })
}