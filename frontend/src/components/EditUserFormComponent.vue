<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        icon="mdi-pencil-box"
        variant="plain"
        text="Add User"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card prepend-icon="mdi-account" title="Edit User">
      <v-card-text>
        <v-form v-model="form.valid">
          <v-row dense>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.username"
                hint="User Name"
                label="User Name*"
                required
                :rules="[rules.nameRules]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.password"
                label="Password*"
                type="password"
                required
                :rules="[rules.pwdRules]"
                @keyup.enter="emitUser"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12">
              <v-select
                :items="timezones"
                label="Timezone*"
                v-model="form.preferences.timezone"
                :rules="[rules.required]"
              >
              </v-select>
            </v-col>

            <v-col cols="12" sm="6">
              <label for="role">Roles</label>
              <v-checkbox
                v-for="(role, index) in availableRoles"
                v-model="form.roles"
                :key="index"
                :value="role"
                :label="role"
                required
                density="compact"
                hide-details
              >
              </v-checkbox>
            </v-col>

            <v-col cols="12" sm="6">
              <label for="active">Is Active?</label>
              <v-radio-group v-model="form.active" name="active">
                <v-radio label="Active" :value="true"></v-radio>
                <v-radio label="Inactive" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
        </v-form>
        <slot></slot>

        <small class="text-caption text-medium-emphasis">*indicates required field</small>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

        <v-btn
          :disabled="!form.valid"
          color="primary"
          text="Update"
          variant="tonal"
          @click="emitUser"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const dialog = ref(false)

const props = defineProps({
  user: {
    username: '',
    roles: {
      type: Array,
      require: true,
    },
    active: false,
    password: '',
    preferences: {
      timezone: '',
    },
  },
})

onMounted(() => {
  form.value = setForm(props.user)
})

const setForm = (user) => ({
  username: user.username,
  password: user.password,
  roles: [...user.roles],
  active: user.active,
  preferences: { timezone: user.preferences?.timezone },
})

const emit = defineEmits(['edit-user'])
const availableRoles = ref(['admin', 'manager', 'tester'])
const timezones = ref(Intl.supportedValuesOf('timeZone'))
const form = ref({
  valid: false,
  username: '',
  password: '',
  roles: [],
  active: false,
  preferences: {
    timezone: '',
  },
})

const rules = ref({
  nameRules: (value) => {
    if (!value) return 'Name is required'
    if (value?.length < 2) return 'Name must have at least 2 caracters'
    return true
  },
  pwdRules: (value) => {
    if (!value) return 'Password is required'
    if (value?.length < 6) return 'Name must have at least 6 caracters'
    return true
  },
  required: (v) => !!v || 'Field is required',
})

const emitUser = () => {
  const payload = form.value.valid ? createPayload(form.value) : null

  dialog.value = false
  emit('edit-user', payload)
  resetForm()
}

const createPayload = ({ username, roles, active, password, preferences }) => ({
  _id: props.user._id,
  username,
  roles,
  active,
  password,
  preferences: {
    timezone: preferences?.timezone,
  },
})

const defaultForm = () => ({
  username: '',
  password: '',
  roles: [],
  active: false,
  preferences: { timezone: '' },
})

const resetForm = () => {
  form.value = defaultForm()
}
</script>
