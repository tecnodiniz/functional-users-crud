<template>
  <v-row>
    <v-col class="text-center">
      <UserFormComponent @new-user="createUser" />
      <UserTableComponent :users="users" @delete-user="handleDelete" @edit-user="handleEdit" />

      <DialogComponet :dialog="dialog" :text="d_text" :title="d_title" @close="dialog = false" />

      <ConfirmDialogComponent
        :dialog="confirm"
        :del="delUser"
        :text="d_text"
        :title="d_title"
        @close="confirm = false"
        @confirm="updateUser"
        @confirm-delete="deleteUser"
      />
    </v-col>
  </v-row>
</template>

<script setup>
import ConfirmDialogComponent from '@/components/ConfirmDialogComponent.vue'
import DialogComponet from '@/components/DialogComponet.vue'
import UserFormComponent from '@/components/UserFormComponent.vue'
import UserTableComponent from '@/components/UserTableComponent.vue'
import { get_users, new_user, update_user, user_delete } from '@/services/api'
import { onMounted, ref } from 'vue'

const users = ref([])
const user = ref({})
const dialog = ref(false)
const confirm = ref(false)
const delUser = ref(false)

const d_title = ref('')
const d_text = ref('')

onMounted(() => {
  getUsers()
})

const createUser = (payload) => {
  new_user(payload)
    .then((response) => {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      getUsers()
    })
    .catch((error) => errorHandler(error))
}
const getUsers = async () => {
  get_users()
    .then((response) => users.value.splice(0, users.value.length, ...response.data))
    .catch((error) => errorHandler(error))
}

const handleEdit = (payload) => {
  user.value = payload
  d_text.value = 'Update confirm'
  d_title.value = 'Confirm action'
  confirm.value = true
  dialog.value = false
}
const updateUser = () => {
  const id = user.value._id
  delete user.value._id

  update_user(id, user.value)
    .then((response) => {
      d_text.value = response.data.msg
      d_title.value = 'Message'
      dialog.value = true
      confirm.value = false

      getUsers()
    })
    .catch((error) => errorHandler(error))
}
const errorHandler = (error) => {
  d_text.value = error.message
  d_title.value = 'Error'
  dialog.value = true
}

const handleDelete = (id) => {
  user.value = id
  d_text.value = 'Delete confirm'
  d_title.value = 'Confirm action'
  confirm.value = true
  dialog.value = false
  delUser.value = true
}

const deleteUser = () => {
  user_delete(user.value).then((response) => {
    d_text.value = response.data.msg
    d_title.value = 'Message'
    dialog.value = true
    confirm.value = false
    delUser.value = false

    getUsers()
  })
}
</script>
