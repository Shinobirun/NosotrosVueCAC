<template>
    <div>
    <h1>Hora actual en {{ city }}:</h1>
    <p>{{ current_time }}</p>
    <button @click="fetchTime">Actualizar Hora</button>
    </div>
</template>

<script>
export default {
    data() {
    return {
        current_time: "",
        city: "America/Argentina/Buenos_Aires",
    };
    },
    mounted() {
    this.fetchTime();
    },
    methods: {
    fetchTime() {
        const url =
        "http://worldtimeapi.org/api/timezone/America/Argentina/Buenos_Aires";

    fetch(url)
        .then((response) => {
            if (response.status === 200) {
            return response.json();
            } else {
            console.error(
                `Error en la solicitud. Código de estado: ${response.status}`
            );
            }
        })
        .then((data) => {
            if (data) {
            this.current_time = data.datetime;
            }
        })
        .catch((error) => {
            console.error("Error al obtener la hora:", error);
        });
    },
    },
};
</script>
