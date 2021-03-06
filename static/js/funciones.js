/**
 * @brief Función que actualiza los datos de combos dependientes
 * @param opcion Código del elemento seleccionado por el cual se filtrarán los datos en el combo dependiente
 * @param app Nombre de la aplicación en la cual buscar la información a filtrar
 * @param mod Modelo del cual se van a extraer los datos filtrados según la selección
 * @param campo Nombre del campo con el cual realizar el filtro de los datos
 * @param n_value Nombre del campo que contendra el valor de cada opción en el combo
 * @param n_text Nombre del campo que contendrá el texto en cada opción del combo
 * @param combo_destino Identificador del combo en el cual se van a mostrar los datos filtrados
 * @param bd Nombre de la base de datos, si no se específica se asigna el valor por defecto
 */
function actualizar_combo(opcion, app, mod, campo, n_value, n_text, combo_destino, bd) {
    /* Verifica si el parámetro esta definido, en caso contrario establece el valor por defecto */
    bd = typeof bd !== 'undefined' ? bd : 'default';
    $.ajaxSetup({
        async: false
    });
    $.getJSON(URL_ACTUALIZAR_COMBO, {
        opcion:opcion, app:app, mod:mod, campo:campo, n_value:n_value, n_text: n_text, bd:bd
    }, function(datos) {

        var combo = $("#"+combo_destino);

        if (datos.resultado) {

            if (datos.combo_disabled == "false") {
                combo.removeAttr("disabled");
            }
            else {
                combo.attr("disabled", "true");
            }

            combo.html(datos.combo_html);
        }
        else {
            bootbox.alert(datos.error);
            console.log(datos.error);
        }
    }).fail(function(jqxhr, textStatus, error) {
        var err = textStatus + ", " + error;
        bootbox.alert( 'Petición fállida' + err );
        console.log('Petición fállida ' + err)
    });
}

/**
 * Función para cambiar la contraseña
 * @param event Recibe el evento
**/
function change_password(event) {
    event.preventDefault();
    if($('#id_old_password').val()=='' || $('#id_new_password').val()=='' || $('#id_new_password_repeat').val()==''){
        MaterialDialog.alert('Debes llenar todos los campos',{'title':'Alerta'});
    }
    else if($('#id_new_password').val()!==$('#id_new_password_repeat').val()){
        MaterialDialog.alert('Las contraseñas no coinciden',{'title':'Alerta'});
    }
    else{
        $.ajax({
            data: $('.change_form').serialize(), 
            type: 'POST',
            url: URL_CHANGE_PASSWORD,
            success: function(response) {
                if (response.success) {
                    MaterialDialog.alert(response.mensaje,{'title':'Éxito'});
                }
                else{
                    MaterialDialog.alert(response.mensaje,{'title':'Error'});
                }
            }
        });
    } 
}