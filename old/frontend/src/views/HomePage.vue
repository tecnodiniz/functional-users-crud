<template>
    <v-btn
        color="primary mb-4"
        @click="overlay = !overlay"
      >
        New User
      </v-btn>
      
  <v-overlay class="align-center justify-center" v-model="overlay" >
    <CreateUserForm @emit-data="createUser" />
  </v-overlay>

  <v-dialog
      v-model="dialog"
      width="auto"
    >
        <v-card
          max-width="400"
          prepend-icon="mdi-update"
          text="User successfully created"
          title="Success"
        >
          <template v-slot:actions>
            <v-btn
              class="ms-auto"
              text="Ok"
              @click="dialog = false"
            ></v-btn>
          </template>
        </v-card>
    
  </v-dialog>
  <TableContent :users="users" @delete-user="handleId" />

  <v-dialog
      v-model="dialog2"
      width="auto"
    >
        <v-card
          max-width="400"
          prepend-icon="mdi-update"
          text="Are you really sure?"
          title="Delete User?"
        >
          <template v-slot:actions>
            <v-btn
              class="ms-auto"
              text="Confirm"
              @click="deleteUser"
            ></v-btn>

            <v-btn
              class="ms-auto"
              text="Cancel"
              @click="dialog2 = false"
            ></v-btn>
          </template>
        </v-card>
    
  </v-dialog>

  <v-dialog
      v-model="dialog3"
      width="auto"
    >
        <v-card
          max-width="400"
          prepend-icon="mdi-update"
          text="User successfully deleted"
          title="User deleted"
        >
          <template v-slot:actions>

            <v-btn
              class="ms-auto"
              text="Confirm"
              @click="dialog3 = false"
            ></v-btn>
          </template>
        </v-card>
    
  </v-dialog>


</template>

<script>

import CreateUserForm from '@/components/createUserForm/CreateUserForm.vue';
import TableContent from '@/components/tableContent/TableContent.vue';
import { delete_user, get_users, post_user } from '@/services/api';


export default {
  name: 'BaseComponent',
  components:{
    TableContent,
    CreateUserForm,
    
  },
  data(){
    return {
      dialog: false,
      dialog2: false,
      dialog3: false,
      overlay: false,
      delete_id: '',
      users:[],
    }
  },
  mounted(){
    get_users()
      .then((response) =>{
        console.log(response.data)
        this.users = response.data
      })
  },
  methods:{
    createUser(data){
      post_user(data)
        .then((response) => {
          console.log(response)
          this.getUsers();
          this.overlay = false;
          this.dialog = true
        }).catch((error) => console.log(error))

    },
    getUsers(){
      get_users()
      .then((response) =>{
        console.log(response.data)
        this.users = response.data
      })
    },
    handleId(id){
      this.delete_id = id
      this.dialog2 = true
    },
    deleteUser(){
      console.log(this.delete_id)
      this.dialog2 = false
      this.dialog3 = true

      delete_user(this.delete_id)
        .then((response) =>{
          console.log(response.data)
          this.getUsers();
        }).catch((error) => console.log(error))
      

    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
