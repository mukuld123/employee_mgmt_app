import React, { useEffect, useState } from 'react'


function Navbar() {

    const [isLoggedIn, setLoggedIn] = useState(false);

    useEffect(()=>{
        let x = sessionStorage.getItem('token');
        if(x == null) setLoggedIn(false);
        else setLoggedIn(true)
    },[sessionStorage.getItem('token')])
    return (
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Emloyee Management</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarText">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/employee">Details</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/reimbursement">Add Reimbursement</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/all_reimbursements">All Reimbursements</a>
                        </li>
                    </ul>
                    {
                        (isLoggedIn)?<><a class="nav-link" href="/logout">Logout</a></>: 
                        <><span class="navbar-text">
                        <a class="nav-link" href="/login">Login</a>
                    </span>
                    <span class='mx-4'>

                        <a class="nav-link" href="/register">Register</a>
                    </span></>
                    }
                   
                </div>
            </div>
        </nav>
    )
}

export default Navbar