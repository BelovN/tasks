import axios from 'axios'

const API_BASE = 'http://localhost:8000/api/v1/auth'

export async function login({ username, password }) {
    const res = await axios.post(`${API_BASE}/login/`, { username, password })
    saveTokens(res.data)
    return res.data
}

export async function register({ username, password, confirm }) {
    const res = await axios.post(`${API_BASE}/register/`, { username, password, confirm })
    saveTokens(res.data)
    return res.data
}

function saveTokens({ access, refresh }) {
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)
}