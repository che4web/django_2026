export default function toFormData(object) {
    const formData = new FormData()
    Object.entries(object).forEach(([key, value]) => {
        if (value !== '' && value !== null && value !== undefined) {
            formData.append(key, value)
        }
    })
    return formData
}
