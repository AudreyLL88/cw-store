// On scroll animation for edit/add product forms.
const sr = ScrollReveal({
        origin: 'top',
        distance: '80px',
        duration: 2000,
        reset: true
    });
sr.reveal('.product-header', {delay: 400});
sr.reveal('.product-form', {delay: 600, interval: 200});

// Image text set-up in add/edit product forms.
$('#new-image').change(function() {
            var file = $('#new-image')[0].files[0];
            $('#filename').text(`Image will be set to: ${file.name}`);
        });

// Hide sizes if category is not clothing.
var category = $('#id_category');
var has_size = $('#id_has_sizes');
var size_1 = $('#id_size_1');
var size_2 = $('#id_size_2');
var size_3 = $('#id_size_3');
var size_4 = $('#id_size_4');
var size_5 = $('#id_size_5');

function refreshOptions() {
    var values = parseInt(category.val())
    if (values > 3) {
        has_size.attr('disabled', true);
        size_1.attr('disabled', true);
        size_2.attr('disabled', true);
        size_3.attr('disabled', true);
        size_4.attr('disabled', true);
        size_5.attr('disabled', true);
        } else {              
            has_size.attr('disabled', false);
            size_1.attr('disabled', false);
            size_2.attr('disabled', false);
            size_3.attr('disabled', false);
            size_4.attr('disabled', false);
            size_5.attr('disabled', false);
        };
    }
    refreshOptions();

    category.on('change', refreshOptions);