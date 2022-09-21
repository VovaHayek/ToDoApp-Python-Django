function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
}

function deleteTask(e){
    $.ajax({
        url: '',
        type: "POST",
        dataType: 'json',
        data: {
            'deleteTaskId': e
        },
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie('csrftoken'),
        },
        success: (response) => {
            location.reload();
        } 
    })
}

function markAsCompleted(e) {
    $.ajax({
        url: '',
        type: "POST",
        dataType: 'json',
        data: {
            'completeTaskId': e
        },
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (data) => {
            location.reload();
        }
    })
}

function markAsUncompleted(e) {
    $.ajax({
        url: '',
        type: "POST",
        dataType: 'json',
        data: {
            'uncompleteTaskId': e
        },
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (response) => {
            location.reload();
        }
    })
}

$("#tasks-filter-completion").on('change', function(){
    $.ajax({
        url: '',
        type: "GET",
        dataType: 'json',
        data: {
            "filterValue": this.value
        },
        headers: {
            "X-Requested-With": 'XMLHttpRequest'
        },
        success: (response) => {
            $("#all-tasks-container").empty('');
            $.each(JSON.parse(response), function(key, value){
                if (value.fields.completion === false){
                    $("#all-tasks-container").append(`<div class="task-container">\
                                        <div class="task-delete-button-container">
                                            <button value="`+value.pk+`" onclick="deleteTask(this.value)"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                        <div class="task-text-container">
                                            <h3>`+value.fields.to_do+`</h3>
                                        </div>
                                        <div class="task-complete-button-container">
                                            <button value="`+value.pk+`" onclick="markAsCompleted(this.value)"></button>
                                        </div>
                                    </div>`);
                } else {
                    $("#all-tasks-container").append(`<div class="task-container completed">\
                                        <div class="task-delete-button-container">
                                            <button value="`+value.pk+`" onclick="deleteTask(this.value)"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                        <div class="task-text-container">
                                            <h3>`+value.fields.to_do+`</h3>
                                        </div>
                                        <div class="task-complete-button-container">
                                            <button value="`+value.pk+`" onclick="markAsUncompleted(this.value)"><i class="fa-solid fa-square-check"></i></button>
                                        </div>
                                    </div>`);
                }
            })
        }
    })
})  