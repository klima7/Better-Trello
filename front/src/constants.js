export default {
    BACKEND_URL: process.env.VUE_APP_LOCAL == "true" ? "http://localhost:5000" : "https://pawtrello.herokuapp.com/"
}
