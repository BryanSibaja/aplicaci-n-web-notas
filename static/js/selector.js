$(document).ready(function()
{
    initialise();
});

function aux() {

    CKEDITOR.config.toolbar = [
        ['Bold', 'Italic', 'Underline'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['Link', 'Unlink'],
        ['RemoveFormat', 'Source']
    ]
    CKEDITOR.replace('editor1');
}

function initialise() {
    $('#eviarC').click(function (event) {
        $.ajax({
            data: { cua: $('#cuadernoN').val() },
            type: 'POST',
            url: 'nuevo/',
            success: function (json) {
                $("#selector").empty()
                $.each(json, function (i, libro) {
                    $("#selector").append(
                        '<option value=' + libro.pk + ' class="list-group-item">' + libro.fields.nombre + '</option>'
                    )
                })
                initialise()
            },
        })
    });

    $('.list-group option').click(
        function barra(e) {
            e.preventDefault()
            $that = $(this)
            $that.parent().find('option').removeClass('active')
            $that.addClass('active')
            $("#id_libro").val($that.val())

            $.ajax({
                url: "notas/",
                type: "POST",
                data: { libro: $("#id_libro").val() },
                success: function (json) {
                    $("#notas").empty()
                    $.each(json, function (i, nota) {
                        $("#notas").append(
                            '<div class="list-group-item list-group-item-action flex-column align-items-start">' +
                            '<div class="d-flex w-100 justify-content-between">' +
                            '<h5 class="mb-1">' + nota.fields.titulo + '</h5>' +
                            '<small class="text-muted">' + nota.fields.creacion + '</small>' +
                            '</div>' +
                            '<p class="mb-1">' + nota.fields.cuerpo + '</p>' +
                            '<small class="text-muted"><button type="button" class="btn btn-link" onclick="eliminarNota('+nota.pk+')">Eliminar</button></small>' +
                            '</div>'
                        )
                    })
                },

                error: function (xhr, errmsg, err) {
                }
            });

        }
    );
}

function eliminarNota(idNota) {
    $.ajax({
        data: { id: idNota },
        type: 'POST',
        url: 'eliminar/',
        success: function (json) {
            $("#notas").empty()
            $.each(json, function (i, nota) {
                $("#notas").append(
                    '<div class="list-group-item list-group-item-action flex-column align-items-start">' +
                    '<div class="d-flex w-100 justify-content-between">' +
                    '<h5 class="mb-1">' + nota.fields.titulo + '</h5>' +
                    '<small class="text-muted">' + nota.fields.creacion + '</small>' +
                    '</div>' +
                    '<p class="mb-1">' + nota.fields.cuerpo + '</p>' +
                    '<small class="text-muted"><button type="button" class="btn btn-link" onclick="eliminarNota(' + nota.pk + ')">Eliminar</button></small>' +
                    '</div>'
                )
            })
        },
    })
}