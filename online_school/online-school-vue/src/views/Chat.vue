<script setup>
import { ref } from 'vue'

const roomName = 'test_room'
const chatSocket = new WebSocket('ws://127.0.0.1:8000' + '/ws/chat/' + roomName + '/')

const messges = ref([])
const message = ref('')

chatSocket.onopen = function () {
    console.info('Chat socket connected')
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    messges.value.push(data.message)
}
chatSocket.onerror = function (e) {
    console.error('Chat socket error', e)
}
chatSocket.onclose = function () {
    console.error('Chat socket closed unexpectedly')
}

function sendMessage() {
    const text = message.value.trim()
    if (!text || chatSocket.readyState !== WebSocket.OPEN) return

    chatSocket.send(JSON.stringify({ message: text }))
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
