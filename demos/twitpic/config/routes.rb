Twitpic::Application.routes.draw do
  root :to => 'root#index'
  get 'save', :to => 'twitpic#show', :as => 'show'
  get 'auth/twitter/callback', :to => 'twitpic#callback', :as => 'callback'
  get 'auth/failure', :to => 'twitpic#error', :as => 'failure'
  post 'twitpic/upload', :to => 'twitpic#upload', :as => 'upload'
  delete 'logout', :to => 'twitpic#destroy', :as => 'logout'
end
