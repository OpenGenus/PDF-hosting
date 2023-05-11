$(document).ready(function() {
    const base_url = "http://localhost:8000/library";
    const book_upload_form = $("#book-upload-form");
    const book_upload_form_submit_btn = $(".book-upload-form-submit");
    let authors_select_options = {
        ajax: {
            dataType: "json",
            delay: 350,
            url: `${base_url}/authors/search`,
            data: function(params) {
                return { q: params.term }
            },
            processResults: process_results,
            cache: true,
        },
        placeholder: "Type to search",
        minimumInputLength: 1,
        tags: true,
        multiple: true
    };

    $(".authors-select").select2(authors_select_options);
    let categories_select_options = $.extend({}, authors_select_options);
    categories_select_options.ajax.url = `${base_url}/book-categories/search`
    $(".categories-select").select2(categories_select_options);

    book_upload_form.submit(function(event) {
    });
    book_upload_form_submit_btn.click(function() {
        book_upload_form.submit();
    });
});

let process_results = (data, params) => {
    let results = data.map((item) => {
        item.text = item.name;
        delete item.name;
        return item;
    });
    return {"results": results};
}
