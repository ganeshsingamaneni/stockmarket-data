
if (window.location.href.includes('index')) {
    (function () {
        fetch('http://localhost:5000/api/getrole/Administrator')
            .then(response => response.json())
            .then(data => {
                if (!data.success && window.location.href.includes('index')) {
                    console.log(data)
                    window.location.href = './adminstratorCreate.html';
                }
            });
    }())

    document.getElementById('formId').addEventListener("submit", function (e) {
        e.preventDefault();
        const email = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        fetch("http://localhost:5000/api/login", {
            method: "POST",
            body: JSON.stringify({ email, password }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(response => response.json())
            .then(res => {
                if (res.success) {
                    localStorage.setItem('userDetails', JSON.stringify(res.data));
                    window.location.href = './rolecreation.html';
                } else { window.alert('Please enter valid credentials'); }
            });

    })
} else if (window.location.href.includes('rolecreation')) {
    document.getElementById('addUserForm').addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById('userName').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const roleId = document.getElementById('rolesRef').value;
        fetch("http://localhost:5000/api/users", {
            method: "POST",
            body: JSON.stringify({
                name, email, password, roleId
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(resp => resp.json())
            .then(data => {
                if (data.success) {
                    $("addUserModal").modal('hide');
                } else { window.alert(data.message); }
            });
    });
} else {
    document.getElementById('createrId').addEventListener("submit", function (e) {
        fetch("http://localhost:5000/api/roles", {
            method: "POST",
            body: JSON.stringify({
                name: "Administrator",
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(respon => respon.json())
            .then(json => {
                if (json.success) {
                    fetch("http://localhost:5000/api/users", {
                        method: "POST",
                        body: JSON.stringify({
                            name: document.getElementById('username').value,
                            email: document.getElementById('email').value,
                            password: document.getElementById('password').value,
                            roleId: json.data.id
                        }),
                        headers: {
                            "Content-type": "application/json; charset=UTF-8"
                        }
                    }).then(resp => resp.json())
                        .then(dat => {
                            if (dat.success) {
                                localStorage.setItem('userDetails', JSON.stringify(dat.data));
                                window.location.href = './rolecreation.html';
                            }
                        });
                }
            });
        e.preventDefault();
    })
}

function addRole() {
    const roleModal = new bootstrap.Modal(document.getElementById('addRoleModal'));
    const roleName = document.getElementById('roleName').value;
    fetch("http://localhost:5000/api/roles", {
        method: "POST",
        body: JSON.stringify({
            name: roleName
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(resp => resp.json())
        .then(data => {
            if (data.success) {
                // $(document).ready(function () {
                // $('#addRoleModal').modal('hide')
                // (document.getElementById('addRoleModal').style.display = 'none')

                // })
                // roleModal.classList.remove("#addRoleModal");
                //    $("#addRoleModal").modal('hide');
            } else {
                window.alert(data.message);
                //  $("#addRoleModal").modal('hide');
                // bootstrap.modal.close();

            }
        });
}

