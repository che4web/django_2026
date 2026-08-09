<script setup>
import { wsconnect } from '@nats-io/nats-core'
import { ref, onMounted } from 'vue'

const roomName = 'test_room'
let nc
const subs = async () => {
    nc = await wsconnect({ servers: ['ws://127.0.0.1:8443'] })
    const sub = nc.subscribe(roomName)
    for await (const msg of sub) {
        const data = JSON.parse(msg.string())
        messges.value.push(data.message)
    }
}
onMounted(() => {
    subs()
})

const messges = ref([])
const message = ref('')

function sendMessage() {
    const text = message.value.trim()

    nc.publish(roomName, JSON.stringify({ message: text }))
    message.value = ''
}
</script>
<template>
    <h1>Chat</h1>
    <div v-for="(m, index) in messges" :key="index">{{ m }}</div>
    <form @submit.prevent="sendMessage">
        <input v-model="message" placeholder="Message" />
        <button type="submit">Send</button>
    </form>
</template>
